from django.contrib import admin
from django.urls import path
from crudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentList/', views.GetStudentsList),
    path('CreateStudent/', views.CreateStudentView),
    path('DeleteStudent/<id>', views.DeleteStudentView),
    path('EditStudent/<id>', views.EditStudentView)
]