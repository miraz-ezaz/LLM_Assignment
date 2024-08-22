from django.core.management.base import BaseCommand
from contentUpdater.services.ollama_service import OllamaService
from contentUpdater.models import Hotel, Summary


class Command(BaseCommand):
    help = 'Summarize the description for all properties in the Hotel table.'

    def handle(self, *args, **kwargs):
        ollama_service = OllamaService()  # Initialize your service class

        hotels = Hotel.objects.all()
        for hotel in hotels:
            summary_text = ollama_service.summarize(hotel.description)
            summary, created = Summary.objects.get_or_create(hotel=hotel)
            summary.summary = summary_text
            summary.save()

            self.stdout.write(self.style.SUCCESS(
                f'Summarized content for property ID {hotel.property_id}.'))

        self.stdout.write(self.style.SUCCESS(
            'Successfully summarized descriptions for all properties.'))
