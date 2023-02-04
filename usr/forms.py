from django import forms

from main.models import Profile, Order

class UsrUpdateForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time', 'total_passenger', 'can_share']