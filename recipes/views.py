from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name='recipes/pages/home.html',
    )


def recipe(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name='recipes/pages/home.html',
    )
