from django.shortcuts import render
from django.views import *
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse,reverse_lazy
# Create your views here.

class index(ListView):
    template_name="index.html"
    model = Student
    
class InsertData(CreateView):
    template_name="insert.html"
    form_class=StudentForm
    success_url=reverse_lazy("index")
