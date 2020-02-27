from django .shortcuts import render, get_object_or_404
from .models import Person


def index(request):
    return render(request, 'profile_app/index.html', locals())