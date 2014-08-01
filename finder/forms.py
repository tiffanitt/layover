from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from finder.models import Event, Member
from django import forms

__author__ = 'TTruong'

class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = Member
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "age", "gender")
        
        # This whole function needs to be indented to the left by one tab, it's too far over.
        # It should be part of 'EmailUserCreationForm' not 'class Meta'
        def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                Member.objects.get(username=username)
            except Member.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',)

# class InputForm(forms.Form):
#     airlines =[('AA','AA'),
#               ('DL','DL'),
#               ('UA','UA'),
#               ('WN','WN'),
#               ('AC','AC'),
#               ('B6','B6'),
#               ('AS','AS'),
#               ('WS','WS'),
#               ('NK','NK'),
#               ('F9','F9'),
#               ('VX','VX'),
#               ('G4','G4'),]
#     airline = forms.ChoiceField(choices=airlines, help_text="iataCode only")
#     flight_number = forms.CharField(max_length=20)
#     month = forms.ChoiceField(choices=[(z,z) for z in range(01,13)])
#     day = forms.ChoiceField(choices=[(x,x) for x in range(1,32)])
#     year = forms.ChoiceField(choices=[(y,y) for y in range(2014,2021)])

class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ["name", 'category']
