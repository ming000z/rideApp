from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from django.utils import timezone

from main.models import Profile, Order
from .forms import ProfileForm, DriverAcceptForm
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

  def get_success_url(self):
    return reverse('driver:driver-main', args=[self.request.user.id])
  
  def get_object(self):
    id_ = self.request.user.id
    return get_object_or_404(Profile, user_id=id_)
  
  def form_valid(self, form):
    form.instance.is_driver = True
    return super().form_valid(form)
  
  
class DriverProfileView(DetailView):
  template_name = 'driver/driver_profile.html'
  model = Profile

  def get_object(self):
    id_ = self.request.user.id
    return get_object_or_404(Profile, user_id=id_)
  
class DriverHomeView(DetailView):
  template_name = 'driver/driver_home.html'
  model = Profile
  
  def get_object(self):
    id_ = self.request.user.id
    return get_object_or_404(Profile, user_id=id_)
  
  def get_context_data(self, **kwargs) :
    orders = super().get_context_data(**kwargs)
    orders['driver_in_trip_order'] = Order.objects.filter(driver_id=self.request.user.id, trip_status=3)
    orders['driver_confirm_order'] = Order.objects.filter(driver_id=self.request.user.id, trip_status=2)
    return orders


class DriverSearchView(ListView):
  template_name = 'driver/driver_order.html'
  model = Order
  form_class = DriverAcceptForm
  
  
  
  def get_context_data(self, **kwargs) :
    orders = super().get_context_data(**kwargs)
    orders['open_order'] = Order.objects.filter(trip_status=1)
    return orders