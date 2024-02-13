from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import status
from .serializers import AuthorSerializer, WorkSerializer, ClientSerializer, LoanSerializer
from .models import Author, Work, Client, Loan
from datetime import date, timedelta


class SearchAPIView(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('query', '')
        search_by = request.query_params.get('search_by', 'author')

        if search_by == 'author':
            results = Author.objects.filter(name__icontains=query)
            serializer = AuthorSerializer(results, many=True)
        elif search_by == 'work':
            results = Work.objects.filter(title__icontains=query)
            serializer = WorkSerializer(results, many=True)
        else:
            results = Client.objects.filter(name__icontains=query)
            serializer = ClientSerializer(results, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoansListAPIView(ListAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


class ClientDetailAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
