from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
  form_class = ProfileForm
  queryset = Profile.objects.all()
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_)
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
  
class DriverDetailView(DetailView):
  template_name = 'driver/driver_profile.html'

  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_)
  