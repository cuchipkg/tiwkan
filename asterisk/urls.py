from django.urls import path
from . import views
urlpatterns = [
    path('softphone/', views.softphone),
]