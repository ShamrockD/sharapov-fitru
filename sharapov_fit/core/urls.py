from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import open_home_page

urlpatterns = [
    path('', open_home_page),
]