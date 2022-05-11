from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    return HttpResponse('<h1>Olá {} de {} anos</h1>'.format(nome, idade))
