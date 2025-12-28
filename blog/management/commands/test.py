from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Just testing new cmd"
    def handle(self, *args, **options):
        a, b = 10, 20
        c = a+b
        print(c)
        self.stdout.write(self.style.SUCCESS("Test Completed..."))