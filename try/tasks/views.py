from django.shortcuts import render
from django import  forms
from django.http import HttpResponseRedirect
from django.urls import reverse
#tasks=["foo","bar", "baz"]
# creating a class to store form data
class newtaskform(forms.Form):
    task=forms.CharField(label="new task")
   # priority=forms.IntegerField(label="priority",min_value=1,max_value=3)


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request , "tasks/index.html",{
        "tasks": request.session["tasks"]
    })



def add(request):
    if request.method=='POST':
        form= newtaskform(request.POST)
 # this is done to check validatidty of data
        if form.is_valid():
            task= form.cleaned_data["task"]
           # tasks.append(task)
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
# here server side validation is done if things are changed in server
#here wrong form is resubmitted back to html
        else:
            return render(request, "tasks/add.html",{
                "form":form
            })
# here empty form is given to html
    return render(request,"tasks/add.html",{
        "form":newtaskform()
    })