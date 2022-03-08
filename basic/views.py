from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'ninja'
        return context
    
class StudentView(DetailView):
    context_object_name = 'schools'
    model = models.Student
    template_name = 'basic/students.html'
    
class SchoolView(ListView):
    context_object_name = 'students'
    model = models.School
    template_name = 'basic/schools.html'
    