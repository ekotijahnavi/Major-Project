# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.contrib import messages
from .forms import SignupForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound
from .functions import handle_uploaded_file
from .models import FeedBack,Contact,Abstracts,Eceabstract,Cseab,Civilabstract,Mechabstract
from .models import Cseproject,Eceproject,Civilproject,Mechproject
# Create your views here.
def loginaction(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            passwd=fm.cleaned_data['password']
            user= authenticate(username=uname,password=passwd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('home')
            else:
                messages.error(request,'please Enter correct username and password')
                return HttpResponseRedirect('login')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})
def signupaction(request):
    if request.method == "POST" :
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully')
            fm.save()
            fm=SignupForm()
    else:
        fm = SignupForm()
    return render(request,'signup.html',{'form':fm})
def home(request):
    return render(request,"home.html")
def projectideas(request):
    return render(request,'projectideas.html')

def pdf_view(request):
    fs=FileSystemStorage()
    filename ='mypdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            response['content-Disposition']='inline; filename=mypdf.pdf'
            return response
    else:
        return HttpResponseNotFound("the request pdf is not found in the server")
def abstract(request):
    if request.method=='POST':
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Abstract Submitted successfully')
            obj=Eceabstract()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Eceabstract.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'abstract.html',context=my_dict)
def cseabstract(request):
    if request.method=='POST':
           
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Abstract Submitted successfully')
            obj=Cseab()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Cseab.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'cseabstract.html',context=my_dict)
def civilabstract(request):
    if request.method=='POST':
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Abstract Submitted successfully')
            obj=Civilabstract()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Civilabstract.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'cseabstract.html',context=my_dict)
def civilabstract(request):
    if request.method=='POST':
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Abstract Submitted successfully')
            obj=Civilabstract()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Civilabstract.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'cseabstract.html',context=my_dict)
def mechabstract(request):
    if request.method=='POST':
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Abstract Submitted successfully')
            obj=Mechabstract()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Mechabstract.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'mechabstract.html',context=my_dict)
def cseproject(request):
    if request.method=='POST':
           
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Project Submitted successfully')
            obj=Cseproject()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Cseproject.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'cseproject.html',context=my_dict)  
def eceproject(request):
    if request.method=='POST':
           
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Project Submitted successfully')
            obj=Eceproject()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Eceproject.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'eceproject.html',context=my_dict) 
def civilproject(request):
    if request.method=='POST':
           
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Project Submitted successfully')
            obj=Civilproject()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Civilproject.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'civilproject.html',context=my_dict)
def mechproject(request):
    if request.method=='POST':
           
            Name=request.POST['name']
            Email=request.POST['email']
            Project=request.POST['project']
            Abstract=request.POST['abstract']
            messages.success(request,'Project Submitted successfully')
            obj=Mechproject()
            obj.Name=Name
            obj.Email=Email
            obj.Project=Project
            obj.Abstract=Abstract
            obj.save()
           
    ab = serializers.serialize("python",Mechproject.objects.all())
    my_dict={
        'ab': ab,
    }
    return render(request,'mechproject.html',context=my_dict)  
def prerequisitesview(request):
    return render(request,'prerequisites.html')

#prerequisites view of web development
def preweb(request):
    return render(request,'preweb.html')
def madview(request):
    return render(request,'mad.html')
def premlview(request):
    return render(request,'preml.html')
def cseview(request):
    return render(request,'cse.html')
def eceview(request):
    return render(request,'ece.html')
def prevlsiview(request):
    return render(request,'vlsi.html')
def embeddedview(request):
    return render(request,'embedded.html')
def iotview(request):
    return render(request,'iot.html')
def autocadview(request):
    return render(request,'autocad.html')
def revitview(request):
    return render(request,'revit.html')
def sketchupview(request):
    return render(request,'sketchup.html')
def aboutview(request):
    return render(request,'about.html')
def feedbackview(request):
  
    if request.method=='POST':
            Name=request.POST['name']
            Email=request.POST['email']
            feedback=request.POST['feedback']
            messages.success(request,'Feedback Submitted successfully')
            obj=FeedBack()
            obj.Name=Name
            obj.Email=Email
            obj.feedback=feedback
            obj.save()
           
    data = serializers.serialize("python",FeedBack.objects.all())
    my_dict={
        'data': data,
    }
    return render(request,'feedback.html',context=my_dict)
def contact(request):
    if request.method=='POST':
            Name=request.POST['name']
            Email=request.POST['email']
            Message=request.POST['message']
            messages.success(request,'message had been successfully submitted')
            obj=Contact()
            obj.Name=Name
            obj.Email=Email
            obj.Message=Message
            obj.save()
    return render(request,"contact.html")
