from django.shortcuts import render
from django.http import HttpResponse


def vista(request):
    return HttpResponse('Esta es mi primera vista!')

