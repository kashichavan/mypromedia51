from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def studentview(request):
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
    
    f=StudentForm()
    return render(request,'student.html',context={'form':f})
