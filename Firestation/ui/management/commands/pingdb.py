from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Simple DB ping so Aiven doesn't look idle"

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        self.stdout.write(self.style.SUCCESS("DB ping OK"))
