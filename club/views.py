from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'club/index.html')


def getresource(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})


def resourceview(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'club/resourceview.html', {'resource' : resource})


def getmeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list' : meeting_list})


def meetingview(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingview.html', {'meeting' : meeting})


# form views
@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()

    else:
        form=MeetingForm()

    return render(request, 'club/newmeeting.html', {'form': form})  

@login_required
def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True) 
            post.save()
            form=ResourceForm()  

    else:
        form=ResourceForm()

    return render(request, 'club/newresource.html', {'form': form})  


# login views
def loginMessage(request):
    return render(request, 'club/loginmessage.html')       


def logoutMessage(request):
    return render(request, 'club/logoutmessage.html')              