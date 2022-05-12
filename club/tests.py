from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(meeting_title='Meeting Title')
        self.meeting=Meeting(adgenda='example adgenda', meeting_location='example location') 

    def test_time(self):
         self.date=Meeting(meeting_date='03-22-22')
         self.time=Meeting(meeting_time='2022-02-02 14:30:59')

    def test_typestring(self):
        self.assertEqual(str(self.title), 'Meeting Title')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')



class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.title=Meeting(meeting_title='Meeting Title')
        self.attendence=User(username='exampleUser')
        self.text=MeetingMinutes(minutes_text='text here')

    def test_string(self):
         self.assertEqual(str(self.title), 'Meeting Title')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meeting_minutes')



class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resource_name='Example Name')
        self.resource=Resource(resource_type='audio book', date_entered=datetime.date(2021,4,13), url='http://www.myresourceexample.com', description='example description') 
        self.user=User(username='User1')

    def test_string(self):
        self.assertEqual(str(self.name), 'Example Name')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def setUp(self):
        self.title=Event(event_title='Title of Event')
        self.event=Event(event_date=datetime.date(2022,2,13), location='Example Location', description='example description')
        self.user=User(username='User2')

    def test_string(self):
        self.assertEqual(str(self.title), 'Title of Event')
     
    def test_tablename(self):
         self.assertEqual(str(Event._meta.db_table), 'event')