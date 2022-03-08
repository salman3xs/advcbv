from django.urls import path
from basic import views

app_name = 'basic'

urlpatterns = [
    path('student/',views.StudentListView.as_view(),name='students'),
    path('school/',views.SchoolListView.as_view(),name='schools'),
    path('school/<int:pk>/',views.SchoolDetailsView.as_view(),name='details')
]
