
from django.shortcuts import render
from Specialtopic.models import Student_database, System_database



# Create your views here.

def index(request):
    if request.method=='POST':
        name = request.POST['name']
        usn = request.POST['usn']
        branch = request.POST['branch']
        # print(name,usn,branch)
        ins = Student_database(Student_name=name ,USN=usn)
        ins.save()
        print("data has been returned to db")
    return render(request,'index.html')