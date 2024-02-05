from django.shortcuts import render, get_object_or_404
from .models import Author, Work, Client, Loan
from datetime import date, timedelta


def search(request):
    query = request.GET.get('query', '')
    search_by = request.GET.get('search_by', 'author')

    if search_by == 'author':
        results = Author.objects.filter(name__icontains=query)
    elif search_by == 'work':
        results = Work.objects.filter(title__icontains=query)
    else:
        results = Client.objects.filter(name__icontains=query)

    print(results)

    return render(request, 'search_results.html', {'results': results})


def loans_list(request):
    loans = Loan.objects.all()
    for loan in loans:
        if loan.due_date < date.today():
            loan.is_overdue = True
        elif loan.due_date < date.today() + timedelta(days=7):
            loan.is_due_soon = True
        else:
            loan.is_ok = True
    return render(request, 'loans_list.html', {'loans': loans})


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_detail.html', {'client': client})
