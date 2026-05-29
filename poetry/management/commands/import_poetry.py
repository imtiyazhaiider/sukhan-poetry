import csv

from django.core.management.base import BaseCommand

from poetry.models import Poet, Writing, Category


class Command(BaseCommand):

    help = "Import poetry data from CSV"

    def add_arguments(self, parser):

        parser.add_argument(
            'csv_file',
            type=str
        )

    def handle(self, *args, **kwargs):

        csv_file = kwargs['csv_file']

        self.stdout.write(
            self.style.SUCCESS(
                f"Reading: {csv_file}"
            )
        )

        with open(csv_file, encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:

                # Create or get poet
                poet, _ = Poet.objects.get_or_create(
                    slug=row['poet_slug'],
                    defaults={
                        'name': row['poet_name'],
                        'biography': '',
                    }
                )

                # Create or get writing
                writing, created = Writing.objects.get_or_create(
                    slug=row['writing_slug'],
                    defaults={
                        'title': row['title'],
                        'poet': poet,
                        'content': row['content'],
                        'writing_type': row['writing_type'],
                        'language': row['language'],
                    }
                )

                # Add categories
                categories = row['categories'].split(';')

                for category_name in categories:

                    category_name = category_name.strip()

                    category, _ = Category.objects.get_or_create(
                        name=category_name
                    )

                    writing.categories.add(category)

                if created:

                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created writing: {writing.title}"
                        )
                    )

                else:

                    self.stdout.write(
                        f"Already exists: {writing.title}"
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Import completed successfully!"
            )
        )