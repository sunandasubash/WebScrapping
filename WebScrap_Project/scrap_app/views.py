from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from .models import Table1


# Create your views here.
def home(request):
    if request.method == 'POST':
        enter_link=request.POST.get('page','')
        urls=requests.get(enter_link)
        x=BeautifulSoup(urls.text,'html.parser')

        for links in x.find_all('a'):
            li_add=links.get('href')
            li_name=links.string
            Table1.objects.create(address=li_add,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values=Table1.objects.all()
    return render(request,'index.html',{'data_values': data_values})

def delete_links(request):
    Table1.objects.all().delete()
    return redirect('home')