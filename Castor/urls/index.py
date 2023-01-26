from django.urls import path, include
from Castor.views.index import index


urlpatterns = [
    path("", index, name="index"),
    path("menu/", include("Castor.urls.menu.index")),
]