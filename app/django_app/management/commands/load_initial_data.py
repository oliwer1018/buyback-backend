from django.core.management.base import BaseCommand
from django_app.models import SKU, DefectDeduction
import pandas as pd
import os

SKU_CSV = 'app/data/mock_sku_list_1000.csv'
DEDUCTIONS_CSV = 'app/data/defect_deduction_matrix.csv'


class Command(BaseCommand):
    help = 'Load initial SKUs and defect deductions from CSV files'

    def handle(self, *args, **kwargs):
        self.stdout.write("Loading SKU and defect data...")

        if not os.path.exists(SKU_CSV) or not os.path.exists(DEDUCTIONS_CSV):
            self.stderr.write("CSV file(s) not found.")
            return

        if SKU.objects.exists():
            self.stdout.write("SKU table already has data. Skipping.")
        else:
            sku_df = pd.read_csv(SKU_CSV)
            for _, row in sku_df.iterrows():
                SKU.objects.get_or_create(
                    sku_number=row['sku_number'],
                    defaults={
                        'brand': row['brand'],
                        'model': row['model'],
                        'storage': row['storage'],
                        'color': row['color'],
                        'grade': row['grade'],
                        'battery_condition': row['battery_condition'],
                        'battery_capacity': row['battery_capacity'],
                        'functional_status': row['functional_status'],
                        'max_refurb_price': row['max_refurb_price'],
                        'buybox_price': row['buybox_price'],
                    }
                )
            self.stdout.write(f"Loaded {len(sku_df)} SKUs.")

        if DefectDeduction.objects.exists():
            self.stdout.write("Defect deduction table already has data. Skipping.")
        else:
            ded_df = pd.read_csv(DEDUCTIONS_CSV)
            for _, row in ded_df.iterrows():
                DefectDeduction.objects.get_or_create(
                    defect=row['defect'],
                    defaults={'deduction': row['deduction']}
                )
            self.stdout.write(f"Loaded {len(ded_df)} defect deductions.")
