from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentRegister, StudentApply, StudentList
from .forms import StudentForm, StudentApplyForm, StudentListForm
from django.urls import reverse

def home(request):
    data = StudentRegister.objects.all()
    return render(request, 'home.html', {'data': data})


def StudentRegisterView(request):
    if request.method == "POST":
        sform = StudentForm(request.POST)
        if sform.is_valid():
            sform.save()
            return redirect('/home')
        return HttpResponse('Saved')
    else:
        sform = StudentForm()
        return render(request, 'registration.html', {'sform': sform})


def StudentApplyView(request):
    if request.method == "POST":
        stform = StudentApplyForm(request.POST)
        if stform.is_valid():
            stform.save()
            return redirect('/home')
        return HttpResponse('Saved')
    else:
        stform = StudentApplyForm()
        return render(request, 'apply.html', {'stform': stform})


def StudentListView(request):
    if request.method == "POST":
        stuform = StudentListForm(request.POST)
        if stuform.is_valid():
            stuform.save()
            return redirect('/home')
        return redirect('/detail')
    else:
        stuform = StudentListForm()
        return render(request, 'studentlist.html', {'stuform': stuform})


def detail(request):
    display = StudentRegister.objects.all()
    display1 = StudentApply.objects.all()
    bookdata = {'detail':display, 'detail':display1}

    return render(request, 'detail.html', bookdata)
