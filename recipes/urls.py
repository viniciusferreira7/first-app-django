from django.urls import path

from typing import List, Union
from django.urls.resolvers import URLPattern, URLResolver
from recipes.views import home

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path('', home),
]
