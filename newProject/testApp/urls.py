from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('hi/', views.hi),
    path('welcome/', views.welcome)
]