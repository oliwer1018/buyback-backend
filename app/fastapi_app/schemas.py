from pydantic import BaseModel
from typing import Literal, Optional


class DeviceInfo(BaseModel):
    imei: str
    brand: str
    model: str
    color: str
    storage: str

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "imei": "123456789012345",
                    "brand": "Apple",
                    "model": "iPhone 11",
                    "color": "Red",
                    "storage": "128GB"
                }
            ]
        }


class AssessmentInfo(BaseModel):
    aesthetics_grade: Literal["A+", "A", "B", "C", "D"]
    battery_capacity: int
    battery_condition: str
    screen: str
    face_id: str

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "aesthetics_grade": "B",
                    "battery_capacity": 92,
                    "battery_condition": "Good",
                    "screen": "Working",
                    "face_id": "Broken"
                }
            ]
        }


class SubmitAssessmentRequest(BaseModel):
    evaluator_id: str
    device: DeviceInfo
    assessment: AssessmentInfo
    pricing_method: Optional[Literal["buybox", "refurb"]] = "buybox"  # ✅ Default to buybox

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "evaluator_id": "partner_001",
                    "pricing_method": "refurb",
                    "device": {
                        "imei": "123456789012345",
                        "brand": "Apple",
                        "model": "iPhone 11",
                        "color": "Red",
                        "storage": "128GB"
                    },
                    "assessment": {
                        "aesthetics_grade": "B",
                        "battery_capacity": 92,
                        "battery_condition": "Good",
                        "screen": "Working",
                        "face_id": "Broken"
                    }
                }
            ]
        }
