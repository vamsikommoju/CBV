from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from app1.models import *

# Create your views here.

# def index(request):
#     return render(request,'app1/index.html',{'msg':'This is Index Page'})

class School(TemplateView):
    template_name = 'app1/School.html'
    def get_context_data(self):
        data = {'msg':'this is school page'}
        return data

class faculty(ListView):
    model = Teacher
    context_object_name = 'obj'
    template_name = 'app1/Teacher.html'
    # def get_context_data(self):
    #     data = {'msg':'this is faculty page'}
    #     return data
   
class facinfo(DetailView):
    model = Teacher
    context_object_name = 'obj1'
    template_name = 'app1/facinfo.html'
   
