from django.shortcuts import render, redirect
from .models import Transaction
from .form import TransactionForm
from django.http import HttpResponse
import datetime


def home(request):
    date = {}
    date['transaction']['t1', 't2', 't3']
    date['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'counts/home.html')


def listing(request):
    date = {}
    date['transaction'] = Transaction.objects.all()
    return render(request, 'counts/listing.html', date)


def new_transaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listing')
    return render(request, 'counts/form.html', {'form': form})


def update(request, pk):
    data = {}
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect('listing')
    data['form'] = form
    data['transaction'] = transaction
    return render(request, 'counts/form.html', data)


def delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('listing')

