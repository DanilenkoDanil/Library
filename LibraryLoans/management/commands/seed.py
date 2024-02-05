from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from LibraryLoans.models import Author, Work, Client, Loan
import random


class Command(BaseCommand):
    help = 'Seeds the database with authors, works, clients, and loans'

    def add_authors_and_works(self):
        authors = [
            Author(name="Лев Толстой"),
            Author(name="Федір Достоєвський"),
            Author(name="Вільям Шекспір"),
            Author(name="Франц Кафка"),
            Author(name="Ернест Хемінгуей"),
            Author(name="Джордж Орвелл"),
        ]
        Author.objects.bulk_create(authors)

        works_data = [
            ("Війна і мир", "Лев Толстой"),
            ("Злочин і кара", "Федір Достоєвський"),
            ("Гамлет", "Вільям Шекспір"),
            ("Процес", "Франц Кафка"),
            ("Старий і море", "Ернест Хемінгуей"),
            ("1984", "Джордж Орвелл"),
        ]
        works = [
            Work(title=title, author=Author.objects.get(name=author_name))
            for title, author_name in works_data
        ]
        Work.objects.bulk_create(works)

    def add_clients(self):
        clients = [Client(name="Клієнт " + str(i), email="email@email.com", phone="+380661234567") for i in range(1, 16)]
        Client.objects.bulk_create(clients)

    def add_loans(self):
        clients = list(Client.objects.all())
        works = list(Work.objects.all())
        loans = [
            Loan(
                work=random.choice(works),
                client=random.choice(clients),
                issue_date=timezone.now().date() - timedelta(days=random.randint(1, 60)),
                due_date=timezone.now().date() - timedelta(days=random.randint(-30, 30))
            ) for _ in range(10)
        ]
        Loan.objects.bulk_create(loans)

    def handle(self, *args, **options):
        self.add_authors_and_works()
        self.add_clients()
        self.add_loans()
        self.stdout.write('Successfully seeded the database with authors, works, clients, and loans')
