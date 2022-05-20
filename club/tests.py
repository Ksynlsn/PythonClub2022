from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm, ResourceForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(meeting_title='Meeting Title')
        self.meeting=Meeting(adgenda='example adgenda', meeting_location='example location') 

    def test_time(self):
         self.date=Meeting(meeting_date='03-22-22')
         self.time=Meeting(meeting_time='14:30:59')

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

# form tests
class NewMeetingForm(TestCase):
    def test_meetingForm(self):
        data={
            'meeting_title': 'title example', 
            'meeting_date': '03-22-22', 
            'meeting_time': '14:30:59', 
            'meeting_location': 'example location', 
            'adgenda': 'example adgenda'
            }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)


class NewResourceForm(TestCase):
    def test_resourceForm(self):
        data={
          'resource_name': 'string',
          'resource_type': 'a type here',
          'url': 'http://myfakewebsite.neet',
          'date_entered': '03-22-22',
          'user': 'User1',
          'description': 'description example'
            }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)


class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        # self.title=Meeting.objects.create(meeting_title='Meeting Title')
        self.meeting=Meeting(meeting_title='Meeting Title', adgenda='example adgenda', meeting_location='example location', meeting_date='03-22-22')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/') 