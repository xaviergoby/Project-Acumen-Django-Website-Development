# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField()
    # email = forms.EmailField()
    # the default setting for fields on UserCreationForm is just
    # username, email, and password!
    class Meta(UserCreationForm.Meta):
        # CustomUser model contains all the fields of the default User
        # model which are username,     first_name, last_name, email, password, groups, and more.
        model = CustomUser
        # additional age field set
        # fields = UserCreationForm.Meta.fields + ('age', 'educational_institution_name', 'educational_level',)
        # fields = ['username', 'email', 'password1', 'password2']
        # fields = UserCreationForm.Meta.fields + ('age', 'educational_institution_name', )
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class PorfileInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "age", "educational_institution_name", "educational_level"]
        labels = {"educational_level": _("Current Education Level"),
                  "educational_institution_name": _("Current Educational Institutions Name")}
        help_texts = {"educational_level": _("E.g.: Primary school, Middle school, High school, University etc..."),
                      "educational_institution_name": _("E.g.: Aqumen Highschool, University of Aqumenville etc...")}
    # first_favourite_subject = forms.CharField(max_length=30, required=False)
    # second_favourite_subject = forms.CharField(max_length=30, required=False)
    # age = forms.IntegerField(required=False)