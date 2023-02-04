from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

from .forms import UsrUpdateForm
from main.models import (Profile, Order,User)
# Create your views here.

class UsrProfileView(DetailView):
  template_name = 'usr/usr_profile.html'
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_) 


def usr_order_detail_view(request,id):

  try:
    orders = Order.objects.get(id=id)
  except Profile.DoesNotExist:
    orders = None

  try:
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
  except User.DoesNotExist:
    user = None
    profile = None
    
  context = {
    'user': user,
    'profile': profile,
    'orders' : orders,

  }
  return render(request, 'usr/usr_order_detail.html', context)


class UsrUpdateView(UpdateView):
  template_name = 'usr/usr_order_update.html'
  form_class = UsrUpdateForm
  model = Order
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('main:main-home')
  
class UsrDeleteView(DeleteView):
  
  
  