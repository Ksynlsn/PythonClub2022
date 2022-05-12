from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('getresource/', views.getresource, name="resources"),
    path('resourceview/<int:id>', views.resourceview, name='resource_details'),
   path('getmeetings/', views.getmeeting, name ="meetings"),
   path('meetingview/<int:id>', views.meetingview, name='details'),
   path('newmeeting/', views.newMeeting, name='newmeeting'),
   path('newresource/', views.newResource, name='newresource'),
]