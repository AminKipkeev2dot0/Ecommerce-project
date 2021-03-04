from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request,'shop/home.html')

def about(request):
    return render (request, 'shop/about.html')

# Create your views here.
