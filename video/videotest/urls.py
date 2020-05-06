
from django.contrib import admin
from django.urls import path, include
from app.dashboard import urls as dashboard_urls
from app.client import urls as client_urls
urlpatterns = [
    path('client/', include(client_urls)),
    path('dashboard/', include(dashboard_urls))
]
