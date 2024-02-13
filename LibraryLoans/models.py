from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Loan(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()

    def is_overdue(self):
        return timezone.now().date() > self.due_date

    def is_due_soon(self):
        if self.is_overdue():
            return False
        return 0 < (self.due_date - timezone.now().date()).days <= 7

    def __str__(self):
        return self.work.title + " - " + self.client.name
