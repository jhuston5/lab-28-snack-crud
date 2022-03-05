from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class SnackListView(ListView):
  template_name="snack_list.html"
  model = Snack
  context_object_name = 'snacks'

class SnackDetailView(DetailView):
  template_name = "snack_detail.html"
  model = Snack

class SnackCreateView(CreateView):
  template_name = "snack_create.html"
  model = Snack
  fields = ['name', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
  template_name = "snack_update.html"
  model = Snack
  fields = ['name', 'purchaser', 'description']

class SnackDeleteView(DeleteView):
  template_name = "snack_delete.html"
  model = Snack
  success_url = reverse_lazy('snack_list')
