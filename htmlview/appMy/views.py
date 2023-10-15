from django.shortcuts import render

# Create your views here.

def indexPage(request):
    context = {}
    return render(request, "index.html", context)

def aboutPage(request):
    context = {}
    return render(request, "about.html", context)

def contactPage(request):
    context = {}
    return render(request, "contact.html", context)