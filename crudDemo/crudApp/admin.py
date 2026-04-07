from django.contrib import admin
from crudApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list = ["SNo","SName","SClass","SAddress"]

admin.site.register(Student,StudentAdmin)