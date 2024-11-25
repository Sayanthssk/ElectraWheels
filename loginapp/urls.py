from django.urls import path

from .views import *

urlpatterns = [
    path('/dash',Admin_dashboard.as_view(), name='dash'),
]
