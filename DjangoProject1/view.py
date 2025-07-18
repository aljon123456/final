from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def character(request):
    return render(request, 'character.html')