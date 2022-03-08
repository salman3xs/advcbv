from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'ninja'
        return context

    
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
 
class SchoolDetailsView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic/school_details.html'

class StudentListView(ListView):
    context_object_name = 'student'
    model = models.Student