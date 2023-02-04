from django.urls import path
from .views import UsrProfileView, usr_order_detail_view

app_name = 'usr'

urlpatterns = [
  path('<int:id>/profile', UsrProfileView.as_view() , name='usr-profile'),
  path('<int:id>/orderDetail', usr_order_detail_view, name='usr-order-detail')

]