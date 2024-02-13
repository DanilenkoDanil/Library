from rest_framework import serializers
from .models import Author, Work, Client, Loan
from django.utils import timezone


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()
    is_due_soon = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ('id', 'issue_date', 'due_date', 'work', 'client', 'is_overdue', 'is_due_soon')

    def get_is_overdue(self, obj):
        return timezone.now().date() > obj.due_date

    def get_is_due_soon(self, obj):
        if timezone.now().date() > obj.due_date:
            return False
        return 0 < (obj.due_date - timezone.now().date()).days <= 7
