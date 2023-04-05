from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}

    return render(request,'display_topic.html',d)

def display_webpage(request):

    LOT=Webpage.objects.all()
    d={'webpages':LOT}
    return render(request,'display_webpage.html',d)

def display_AccessRecords(request):
    
    LOT=Access_Records.objects.all()
    d={'accessrecords':LOT}
    return render(request,'display_AccessRecords.html',d)




