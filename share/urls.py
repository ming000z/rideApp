from django.urls import path
from .views import ShareSearchView

app_name = 'share'

urlpatterns = [
  path('search', ShareSearchView.as_view(), name='share-search'),
  # path('<int:id>/profile', UsrProfileView.as_view() , name='usr-profile'),
  # path('order-update/<int:id>', UsrUpdateView.as_view(), name='usr-order-update'),
  # path('order-detail/<int:id>', usr_order_detail_view, name='usr-order-detail'),
  # path('order-delete/<int:id>', UsrDeleteView.as_view(), name='usr-order-delete'),
]