from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from django.utils import timezone

from main.models import Profile
from .forms import ProfileForm
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

# Create your views here.
class DriverUpdateView(UpdateView):
  template_name = 'driver/driver_update.html'
  #form_class = ProfileForm
  #queryset = Profile.objects.all()

  model = Profile
  fields = ['is_driver','type','plante_num','max_passenger','available_status','special_info']
 
  
  def get_success_url(self):
    id_ = self.kwargs.get("id")
    return reverse('driver:driver-profile', kwargs={'id': id_})
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_)
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
  
class DriverDetailView(DetailView):
  template_name = 'driver/driver_profile.html'
  model = Profile

  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_)
  
class DriverMainView(DetailView):
  template_name = 'driver/driver_main.html'

#   def get_object(self):
#     id_ = self.kwargs.get("id")
#     return get_object_or_404(Profile, id=id_)