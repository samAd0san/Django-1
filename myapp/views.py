from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def flipkart(request):
#     return HttpResponse("Hello user welcome to my website..")

# def Amazon(request):
#     return HttpResponse("Hello ma man welcome to amazon")

# def Intel(request):
#     return HttpResponse("Hello ma man welcome to intel")

def fun1(request):
    return render(request,'sample.html')

def mobile(request):
    data = {
        'mobile1' : 'samsung',
        'mobile2' : 'iphone'
    }
    return render(request,'mobile.html',data)

def demo(request):
    return render(request,'index1.html')

def demo1(request):
    return render(request,'index.html')

