from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Update property content'

    # List of available subcommands
    available_subcommands = ['rewrite', 'summarize']

    def add_arguments(self, parser):
        # This adds subcommands as arguments
        parser.add_argument('subcommand', type=str,
                            nargs='?', help='Subcommand to run')

    def handle(self, *args, **options):
        subcommand = options['subcommand']

        if subcommand is None:
            self.stderr.write(self.style.ERROR(
                'Error: No subcommand provided.\n'))
            self.stderr.write(self.style.WARNING('Available subcommands:\n'))
            for cmd in self.available_subcommands:
                self.stderr.write(f'  - {cmd}')
            return

        if subcommand not in self.available_subcommands:
            self.stderr.write(self.style.ERROR(
                f'Error: Invalid subcommand "{subcommand}".\n'))
            self.stderr.write(self.style.WARNING('Available subcommands:\n'))
            for cmd in self.available_subcommands:
                self.stderr.write(f'  - {cmd}')
            return

        try:
            call_command(subcommand)
        except CommandError as e:
            self.stderr.write(self.style.ERROR(f'Error: {str(e)}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
