from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Testing path')


def project(request, pk):
    return HttpResponse('project number' + ' ' + str(pk))

