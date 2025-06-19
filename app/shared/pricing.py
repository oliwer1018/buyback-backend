from django_app.models import SKU, DefectDeduction


def match_sku(device: dict) -> SKU:
    """
    Matches a device to the best available SKU.
    Criteria: brand, model, storage, color
    """
    matches = SKU.objects.filter(
        brand__iexact=device["brand"],
        model__iexact=device["model"],
        storage__iexact=device["storage"],
        color__iexact=device["color"]
    ).order_by('-buybox_price')  # prioritize better priced SKUs

    if not matches.exists():
        raise ValueError("No matching SKU found")

    return matches.first()


def calculate_price(assessment: dict, sku: SKU, method="buybox") -> dict:
    """
    Calculates the price using either 'buybox' or 'refurb' method.
    Applies deductions based on assessment and DB rules.
    """
    notes = []
    price = 0

    if method == "buybox":
        price = 0.8 * float(sku.buybox_price)
        pricing_method = "buybox"

    else:
        price = float(sku.max_refurb_price)
        pricing_method = "refurb"

        # Load all known deductions from DB
        deductions = {d.defect: float(d.deduction) for d in DefectDeduction.objects.all()}

        # Face ID
        if assessment.get("face_id", "").lower() == "broken":
            if "face_id_broken" in deductions:
                price -= deductions["face_id_broken"]
                notes.append(f"Face ID broken: -€{deductions['face_id_broken']}")

        # Screen
        if assessment.get("screen", "").lower() != "working":
            if "screen_not_working" in deductions:
                price -= deductions["screen_not_working"]
                notes.append(f"Screen not working: -€{deductions['screen_not_working']}")

        # Battery capacity
        if assessment.get("battery_capacity", 100) < 90:
            if "battery_capacity_below_90" in deductions:
                price -= deductions["battery_capacity_below_90"]
                notes.append(f"Battery capacity below 90%: -€{deductions['battery_capacity_below_90']}")

        # (optional) add more conditions here...

    return {
        "evaluated_sku": sku.sku_number,
        "price": max(int(price), 0),
        "pricing_method": pricing_method,
        "matched_grade": sku.grade,
        "notes": notes
    }
