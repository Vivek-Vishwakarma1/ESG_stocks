from django.shortcuts import render

# Create your views here.
# stock_list/views.py
from .models import Stock, ESGScore

def stock_list_view(request):
    stocks = Stock.objects.all().select_related('esgscore')
    return render(request, 'stock_list/stock_list.html', {'stocks': stocks})
