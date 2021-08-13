from django.shortcuts import render, redirect
from time import gmtime, strftime


def index(request):
    context = {
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%H:%M:%S", gmtime())
        }
    return render(request, 'index.html', context)


def time_display(request):
    return redirect("/")

