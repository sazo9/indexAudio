# coding: utf-8
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def core(request):
    return HttpResponse('app core')
