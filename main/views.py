from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import Http404

from django.contrib.auth.models import User
from .models import (Profile, Order)
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages  

from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

# Create your views here.

def home_page_view(request):
  try:
    user = User.objects.get(username=request.user.username)
  except User.DoesNotExist:
    user = None
  
  try:
    profile = Profile.objects.get(user=user)
  except Profile.DoesNotExist:
    profile = None
  
  try:
    orders_open = Order.objects.filter(rider_id=request.user.id, trip_status=1)
  except Profile.DoesNotExist:
    orders_open = None
  try:
    orders_comfirme = Order.objects.filter(rider_id=request.user.id, trip_status=2)
  except Profile.DoesNotExist:
    orders_comfirme = None
    
  context = {
    'user': user,
    'profile': profile,
    'orders_open' : orders_open,
    'orders_comfirme' : orders_comfirme
  }
  return render(request, 'main/home_page.html', context)



# Create your views here.
def signup(request):
  if request.method == "POST":
    user_form = NewUserForm(request.POST)
    if user_form.is_valid():
      user = user_form.save()
      Profile.objects.create(user=user)
      login(request, user)
      messages.success(request, "Registration successful.")
      return redirect('main:main-home')
    messages.error(request, "Unsuccessful registration, invalid information")

    
  user_form = NewUserForm()
  context = {
    'form': user_form
  }
  return render(request, "main/sign_up.html", context)
  
def log_in(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('main:main-home')
      else:
        messages.error(request,"Invalid username or password.")
    else:
      print("invalid")
      messages.error(request,"Invalid username or password.")
  form = AuthenticationForm()
  
  context = {
    "form": form
  }
  return render(request, "main/log_in.html", context)


def log_out(request):
  logout(request)
  messages.info(request, "You are succesfully logged out")
  return redirect('main:main-home')
    


  
  
