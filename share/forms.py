from django import forms

from main.models import Profile, Order

    
class ShareJoinOrderForm(forms.ModelForm):
  pass_num = forms.IntegerField(help_text="How many people to join?")
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time', 'total_passenger']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['destination'].disabled = True
    self.fields['arrival_time'].disabled = True
    self.fields['total_passenger'].disabled = True
  
  def save(self, commit: bool = True):
    instance = super().save(commit=False)
    instance.total_passenger += int(self.data.get('pass_num'))
    if commit:
        instance.save()
    return instance