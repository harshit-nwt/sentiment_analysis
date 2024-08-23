import csv
from django.core.management.base import BaseCommand
from ESA.models import Email
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Load email data from a CSV file located in the ESA directory'

    def handle(self, *args, **kwargs):
        # Construct the path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'ESA', 'enr_con.csv')

        # Check if the file exists
        if not os.path.isfile(csv_file_path):
            self.stderr.write(self.style.ERROR(f'File not found: {csv_file_path}'))
            return

        # Increase the field size limit
        csv.field_size_limit(1024 * 1024 * 10)  # 10 MB

        # Open and read the CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Only use the content column
                Email.objects.update_or_create(
                    content=row['content']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
