from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Author, Work, Client, Loan


class SearchAPITestCase(APITestCase):

    def setUp(self):
        Author.objects.create(name="Author 1")
        Work.objects.create(title="Work 1", author=Author.objects.get(name="Author 1"))
        Client.objects.create(name="Client 1")

    def test_search_author(self):
        url = reverse('search')
        response = self.client.get(url, {'query': 'Author 1', 'search_by': 'author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_work(self):
        url = reverse('search')
        response = self.client.get(url, {'query': 'Work 1', 'search_by': 'work'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_client(self):
        url = reverse('search')
        response = self.client.get(url, {'query': 'Client 1', 'search_by': 'client'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class LoansListAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.work = Work.objects.create(title="Work 1", author=self.author)
        self.client_obj = Client.objects.create(name="Client 1")
        Loan.objects.create(work=self.work, client=self.client_obj, issue_date="2023-12-21", due_date="2024-01-21")

    def test_loans_list(self):
        url = reverse('loans')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ClientDetailAPITestCase(APITestCase):

    def setUp(self):
        self.client_obj = Client.objects.create(name="Client 1")

    def test_client_detail(self):
        url = reverse('client', kwargs={'pk': self.client_obj.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.client_obj.name)
