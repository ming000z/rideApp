from django.urls import path

from .views import (DriverUpdateView, DriverDetailView)

app_name = 'driver'
urlpatterns = [
  path('<int:id>/profile', DriverDetailView.as_view(), name='driver-profile'),
  path('<int:id>/signup', DriverUpdateView.as_view(), name='driver-update'),
]