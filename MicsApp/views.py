from django.shortcuts import render
from django.http.response import HttpResponse


def homepage(request):
    return render(request, 'MicsApp/homepage.html')


def blog(request):
    return HttpResponse('Blog for mics.sch')


def assign_lessons(request):
    return HttpResponse('Assign lessons for mics.sch')


def contact_info(request):
    return render(request, 'MicsApp/contact_info.html')
