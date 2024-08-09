from django.shortcuts import render
from .models import Student,Trainer
def home(request):
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def addstudent(request):
    s=Student()
    s.sname=request.POST['sname']
    s.branch=request.POST['branch']
    tid=request.POST['trainer']
    s.trainer=Trainer.objects.get(id=tid)
    s.save();
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
