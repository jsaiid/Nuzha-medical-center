from django.shortcuts import render, redirect
from watad.models import *
from django.views.decorators.csrf import csrf_protect 
from django.views.decorators.csrf import csrf_exempt

from django import forms


# Create your views here.
def home_view(request):
    context={}
    return render(request,"index.html" ,context)

def contact_view(request):
    cont=contact.objects.all()
    context={}
    context["contact"]=cont
    return render(request,"contact.html" ,context)


def our_partners_view(request):
    part=partners.objects.all()
    context={}
    context["partners"]=part
    return render(request,"our_partners.html" ,context)

def strategy_view (request):
    context={}
    return render(request,"strategy.html" ,context)

def presedent_lettre_view (request):
    context={}
    return render(request,"presedent_lettre.html" ,context)

def calls_view (request):
    call=details_job.objects.all()
    context={}
    context["call"]=call
    return render(request,"calls.html" ,context)

def activities_view(request):
    actv=activities.objects.all()
    context={}
    context["activites"]=actv
    return render(request,"activities.html" ,context)

def activity_view (request):
    context={}
    return render(request,"activity.html" ,context)

def newsActivity_view(request):
    context={}
    return render(request,"newsActivity.html" ,context)


def details_job_view (request):
    job=details_job.objects.all()
    context={}
    context["details_job"]=job
    return render(request,"details_job.html" ,context)































    



    
















