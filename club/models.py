from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# MEETING
class Meeting(models.Model):
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    meeting_time = models.DateTimeField()
    meeting_location = models.CharField(max_length=255)
    adgenda = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meeting_title
    
    class Meta:
        db_table='meeting'

# MEETING MINUTES
class MeetingMinutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meeting_id
    
    class Meta:
        db_table='meeting_minutes'

# RESOURCE
class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    url = models.URLField()
    date_entered = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resource_name
    
    class Meta:
        db_table='resource'

# EVENT
class Event(models.Model):
    event_title = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.event_title
    
    class Meta:
        db_table='event'