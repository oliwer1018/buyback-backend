from . import celery_app

from app.shared.pricing import match_sku, calculate_price


@celery_app.task(name="evaluate_device")
def evaluate_device(payload: dict) -> dict:
    """
    Celery task to evaluate a device assessment and return a pricing result.
    """
    try:
        device = payload.get("device", {})
        assessment = payload.get("assessment", {})
        method = payload.get("pricing_method", "buybox")  # optional override

        sku = match_sku(device)
        result = calculate_price(assessment, sku, method=method)

        return result

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
