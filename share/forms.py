from django import forms

from main.models import Profile, Order

    
class ShareSearchOrderForm(forms.ModelForm):
  earlist_arrival = forms.TextInput(attrs={'type': 'datetime-local'});
  latest_arrival = forms.TextInput(attrs={'type': 'datetime-local'});
  
  class Meta:
    model = Order
    fields = ['destination', 'total_passenger']
