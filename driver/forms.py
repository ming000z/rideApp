from django import forms

from main.models import Profile, Order


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'type',
      'plante_num',
      'max_passenger',
      'special_info'
    ]

class DriverAcceptForm(forms.ModelForm):
  accpet = forms.BooleanField(help_text="want to take this order?")
