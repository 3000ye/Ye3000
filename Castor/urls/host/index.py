from django.urls import path
from Castor.views.host.index import index


urlpatterns = [
    path("", index, name="index"),
]
