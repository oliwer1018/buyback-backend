from django.db import models


class SKU(models.Model):
    sku_number = models.CharField(max_length=64, unique=True)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    storage = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    grade = models.CharField(max_length=4)
    battery_condition = models.CharField(max_length=32)
    battery_capacity = models.PositiveIntegerField()
    functional_status = models.CharField(max_length=64)
    max_refurb_price = models.DecimalField(max_digits=10, decimal_places=2)
    buybox_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model} {self.storage} {self.color} ({self.grade})"


class DefectDeduction(models.Model):
    defect = models.CharField(max_length=64, unique=True)
    deduction = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.defect}: -€{self.deduction}"
