from django.urls import path

from .views import (OrderCreateView, OrderListView)

app_name = 'order'

urlpatterns = [
  path("create", OrderCreateView.as_view() , name="order-create"),
  path("", OrderListView.as_view(), name="order-list"),
]