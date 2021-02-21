from django.shortcuts import render
from eventregistration.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Participant

# Create your views here.

def home(request):
    context={}
    return render(request , 'internetofthings/home.html' , context)

def registration(request):
    context={}

    if request.method=='POST':
        p1=Participant()
        p1.name=request.POST.get('name','-')
        p1.phoneno=request.POST.get('phoneno','-')
        p1.email=request.POST.get('email','-')
        p1.institutionname=request.POST.get('institutionname','-')

        if len(Participant.objects.values_list('name',flat=True)) >= 15:
            return render(request,'internetofthings/failure.html',context)
        elif p1.email in Participant.objects.values_list('email',flat=True):
            return render(request,'internetofthings/retry.html',context)
        elif p1.phoneno in Participant.objects.values_list('phoneno',flat=True):        
            return render(request,'internetofthings/retry.html',context)
        else:
            p1.save()
            return render(request,'internetofthings/success.html',context)
    
    if request.method=='GET':
        context['name']=""
        context['phoneno']=""
        context['email']=""
        context['institutionname']=""
    return render(request , 'internetofthings/registration.html' , context)

def listofparticipants(request):
    context={}
    participants=Participant.objects.all()
    context["participants"]=participants
    return render(request , 'internetofthings/listofparticipants.html' , context)
    