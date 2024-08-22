from django.core.management.base import BaseCommand
from contentUpdater.services.ollama_service import OllamaService
from contentUpdater.models import Hotel


class Command(BaseCommand):
    help = 'Rewrite the title and description for all properties in the Hotel table.'

    def handle(self, *args, **kwargs):
        ollama_service = OllamaService()  # Initialize your service class

        hotels = Hotel.objects.all()
        for hotel in hotels:
            new_title = ollama_service.rewrite_title(hotel.title)
            new_description = ollama_service.rewrite_description(
                hotel.description)
            hotel.title = new_title
            hotel.description = new_description
            hotel.save()

            self.stdout.write(self.style.SUCCESS(
                f'Rewrote content for property ID {hotel.property_id}.'))

        self.stdout.write(self.style.SUCCESS(
            'Successfully rewrote titles and descriptions for all properties.'))
