from django import forms

from main.models import Profile, Order
from django.contrib.auth.models import User

    
class ShareJoinOrderForm(forms.ModelForm):
  pass_num = forms.IntegerField(help_text="How many people to join?")
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time', 'total_passenger']
    
  def __init__(self, user, *args, **kwargs):
    self.user = user
    super(ShareJoinOrderForm, self).__init__(*args, **kwargs)
    self.user_id = Profile.get_user_id()
    self.fields['destination'].disabled = True
    self.fields['arrival_time'].disabled = True
    self.fields['total_passenger'].disabled = True
    
  
  def save(self, commit: bool = True):
    instance = super().save(commit=False)
    print(self.data)
    instance.total_passenger += int(self.data.get('pass_num'))
    print(self.user_id)
    instance.share_ids.append(self.user_id)
    if commit:
        instance.save()
    return instance