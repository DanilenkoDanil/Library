from django.test import TestCase, Client as DjangoClient
from django.core.urlresolvers import reverse
from .models import Author, Work, Client, Loan
from datetime import date, timedelta


class LibraryTest(TestCase):

    def setUp(self):
        self.test_client = DjangoClient()
        self.author = Author.objects.create(name="Тестовий Автор")
        self.work = Work.objects.create(title="Тестовий Твір", author=self.author)
        self.client = Client.objects.create(name="Тестовий Клієнт", email="test@example.com", phone="+380661234567")
        self.loan = Loan.objects.create(work=self.work, client=self.client,
                                        issue_date=date.today() - timedelta(days=10),
                                        due_date=date.today() - timedelta(days=5))

    def test_search_view(self):
        response = self.test_client.get(reverse('search'), {'query': self.author.name, 'search_by': 'author'})
        self.assertQuerysetEqual(response.context['results'], [repr(self.author)])

        response = self.test_client.get(reverse('search'), {'query': self.work.title, 'search_by': 'work'})
        self.assertQuerysetEqual(response.context['results'], [repr(self.work)])

        response = self.test_client.get(reverse('search'), {'query': self.client.name, 'search_by': 'client'})
        self.assertQuerysetEqual(response.context['results'], [repr(self.client)])

    def test_loans_list_view(self):
        response = self.test_client.get(reverse('loans_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loans_list.html')
        self.assertTrue(any(loan.is_overdue for loan in response.context['loans']))

    def test_client_detail_view(self):
        response = self.test_client.get(reverse('client_detail', args=[self.client.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client_detail.html')
        self.assertEqual(response.context['client'], self.client)
