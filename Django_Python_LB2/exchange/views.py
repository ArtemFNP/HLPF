from django.shortcuts import render, redirect
from .models import Currency
from .forms import CurrencyForm
from datetime import date

def currency_list(request):
    today = date.today()
    currencies = Currency.objects.filter(date=today)
    form = CurrencyForm()

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('currency_list')

    return render(request, 'exchange/currency_list.html', {'currencies': currencies, 'form': form})
