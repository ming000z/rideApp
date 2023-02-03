from django.urls import path

from .views import (home_page_view, signup, log_in, log_out)

app_name = 'main'

urlpatterns = [
  path("", home_page_view, name="main-home"),
  path("signup", signup, name="signup"),
  path("login", log_in, name="log_in"),
  path("logout", log_out, name="log_out"),
]