from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
)

from main.models import (Profile, Order)
from .forms import ShareSearchOrderForm

class ShareSearchView(ListView):
  model = Order
  template_name = 'share/share_search.html'
  
  
  def get_queryset(self):
    earlist_arrival = self.request.GET.get('earlist_arrival')
    latest_arrival = self.request.GET.get('latest_arrival')
    destination = self.request.GET.get('destination')
    total_passenger = self.request.GET.get('total_passenger')
    
    return Order.objects.filter(can_share=True, arrival_time__gte=earlist_arrival, arrival_time__lte=latest_arrival, destination=destination)
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['form'] = ShareSearchOrderForm()
    print(context['form'])
    return context

