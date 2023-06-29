from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("Home")


def about(request):
    return HttpResponse("About")


def servicies(request):
    return HttpResponse("Servicies")


def store(request):
    return HttpResponse("Store")


def contact(request):
    return HttpResponse("Contact")


def blog(request):
    return HttpResponse("Blog")


def sample(request):
    return HttpResponse("sample")
