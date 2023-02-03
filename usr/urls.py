from django.urls import path
from .views import UsrProfileView

app_name = 'usr'

urlpatterns = [
  path('<int:id>/', UsrProfileView.as_view() , name='usr-profile'),
]