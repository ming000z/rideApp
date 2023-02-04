from django.urls import path

from .views import (DriverUpdateView, DriverProfileView, DriverHomeView)

app_name = 'driver'
urlpatterns = [
  path('<int:pk>', DriverHomeView.as_view(), name='driver-main'),
  path('<int:pk>/profile', DriverProfileView.as_view(), name='driver-profile'),
  path('<int:id>/signup', DriverUpdateView.as_view(), name='driver-update'),
  

]