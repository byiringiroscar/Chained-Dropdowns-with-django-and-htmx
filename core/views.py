from django.shortcuts import render
from .models import Course, Module

# Create your views here.


def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'university.html', context)
