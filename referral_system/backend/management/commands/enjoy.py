from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        image = "🅴🅽🅹🅾🆈"
        print(f'{image}')