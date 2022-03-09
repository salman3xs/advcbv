from django.urls import path
from basic import views

app_name = 'basic'

urlpatterns = [
    path('student/',views.StudentListView.as_view(),name='students'),
    path('school/addstudent/',views.StudentCreateView.as_view(),name='addstudent'),
    path('school/',views.SchoolListView.as_view(),name='schools'),
    path('school/<int:pk>/',views.SchoolDetailsView.as_view(),name='details'),
    path('school/create/',views.SchoolCreateView.as_view(),name='create'),
    path('school/update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('school/delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
]
