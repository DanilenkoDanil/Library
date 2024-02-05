from django.contrib import admin
from .models import Author, Work, Client, Loan


admin.site.register(Author)
admin.site.register(Work)
admin.site.register(Client)
admin.site.register(Loan)
