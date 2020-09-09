from django.shortcuts import render

# Create your views here.
from dynamic.models import Item


def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
