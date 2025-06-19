from fastapi import APIRouter, HTTPException, Path
from app.fastapi_app.schemas import SubmitAssessmentRequest
from app.celery_app.tasks import evaluate_device
from celery.result import AsyncResult

router = APIRouter()


@router.post("/submit-assessment/")
def submit_assessment(payload: SubmitAssessmentRequest):
    """
    Submits a device assessment and returns a Celery task ID for async processing.
    """
    payload = payload.dict(exclude_none=True)
    task = evaluate_device.delay(payload)
    return {"task_id": task.id}


@router.get("/pricing-status/{task_id}")
def pricing_status(task_id: str = Path(..., description="Celery task ID")):
    """
    Checks the status of a previously submitted pricing task.
    """
    result = AsyncResult(task_id)

    if result.state == "PENDING":
        return {"status": "processing"}

    elif result.state == "SUCCESS":
        return {"status": "completed", "result": result.result}

    elif result.state == "FAILURE":
        return {"status": "failed", "error": str(result.result)}

    else:
        return {"status": result.state}
