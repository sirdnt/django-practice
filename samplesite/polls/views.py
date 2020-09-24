from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {"name": "There", "items": ["Movie", "Music", "Karaoke"]}
    return render(request, "polls/index.html", context)
