from django.shortcuts import HttpResponse, render, redirect


def Home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
