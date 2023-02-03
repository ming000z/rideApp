from django.shortcuts import render, get_object_or_404
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

from main.models import Profile
# Create your views here.

class UsrProfileView(DetailView):
  template_name = 'usr/usr_profile.html'
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_) 
