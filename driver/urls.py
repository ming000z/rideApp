from django.urls import path

from .views import (DriverUpdateView, 
                    DriverProfileView, 
                    DriverHomeView, 
                    DriverSearchView,
                    DriverAcceptOrderView,
                    DriverCompleteOrder)

app_name = 'driver'
urlpatterns = [
  path('<int:pk>', DriverHomeView.as_view(), name='driver-main'),
  path('<int:pk>/profile', DriverProfileView.as_view(), name='driver-profile'),
  path('<int:id>/signup', DriverUpdateView.as_view(), name='driver-update'),
  path('find-order', DriverSearchView.as_view(), name='driver-find'),
  path('accept-order/<int:id>', DriverAcceptOrderView.as_view(), name="driver-accpet-order"),
  path('complete-order/<int:id>', DriverCompleteOrder.as_view(), name="driver-complete-order"),
]