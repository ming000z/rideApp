from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  TemplateView
)

from main.models import (Profile, Order)
from .forms import ShareJoinOrderForm

# class ShareSearchView(ListView):
#   model = Order
#   template_name = 'share/share_search.html'
  
  
#   def get_queryset(self):
#     earlist_arrival = self.request.GET.get('earlist_arrival')
#     latest_arrival = self.request.GET.get('latest_arrival')
#     destination = self.request.GET.get('destination')
#     total_passenger = self.request.GET.get('total_passenger')
    
#     return Order.objects.filter(can_share=True, arrival_time__gte=earlist_arrival, arrival_time__lte=latest_arrival, destination=destination)
  
#   def get_context_data(self, *args, **kwargs):
#     context = super().get_context_data(*args, **kwargs)
#     context['form'] = ShareSearchOrderForm(initial={
#             'arrival_time': self.request.GET.get('searrival_timearch', ''),
#             'destination': self.request.GET.get('destination', '')})
#     print(context['form'])
#     return context

class ShareHomeView(TemplateView):
  template_name = 'share/share_home.html'

class ShareSearchResultView(ListView):
  model = Order
  template_name = 'share/share_search_result.html'
  
  def get_queryset(self): 
    des = self.request.GET.get("des")
    earliest_time = self.request.GET.get("earliest-time")
    latest_time = self.request.GET.get("latest-time")
    return Order.objects.filter(destination=des, 
                                arrival_time__range=(earliest_time, latest_time),
                                can_share=True
                                )
  
class ShareJoinOrderView(UpdateView):
  template_name = 'share/share_join.html'
  form_class = ShareJoinOrderForm
  queryset = Order.objects.all()
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('order:order-detail', args=[self.kwargs.get("id")])