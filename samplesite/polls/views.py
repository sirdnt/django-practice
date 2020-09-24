"""
Views
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """Index view"""
    context = {"name": "There", "items": ["Movie", "Music", "Karaoke"]}
    return render(request, "polls/index.html", context)
