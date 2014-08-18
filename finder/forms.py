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


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'category']
