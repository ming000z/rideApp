from django import forms

from main.models import Profile


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'type',
      'plante_num',
      'max_passenger',
      'special_info'
    ]