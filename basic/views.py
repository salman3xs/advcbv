from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
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

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic:schools')


class StudentListView(ListView):
    context_object_name = 'student'
    model = models.Student
    
class StudentCreateView(CreateView):
    model = models.Student
    fields = ('name','age','school')