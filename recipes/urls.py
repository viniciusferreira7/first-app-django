from django.urls import path

from typing import List, Union
from django.urls.resolvers import URLPattern, URLResolver
from recipes import views

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe)
]
