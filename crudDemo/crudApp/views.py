from django.shortcuts import render,redirect
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.
def GetStudentsList(request):
    students = Student.objects.all()  
    return render(request, "crudApp/Index.html",{'studentsList':students})

def CreateStudentView(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/crudApp/StudentList/')

    return render(request,'crudApp/Create.html',{'studentform': form})

def DeleteStudentView(request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('/crudApp/StudentList/')  

def EditStudentView(request,id):
    student = Student.objects.get(id=id)
        
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
             form.save()
        return redirect('/crudApp/StudentList/')

    return render(request,'crudApp/Edit.html',{'student': student})
    