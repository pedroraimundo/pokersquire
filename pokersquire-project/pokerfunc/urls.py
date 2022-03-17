from django.urls import path
from . import views


urlpatterns = [
    path('squire/', views.squire, name='squire'),
    path('settings/', views.squire, name='settings'),
]
