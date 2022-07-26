from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import BloodRequestSession, BloodGroup, UserDetail


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['user', 'blood_group', 'contact_no', 'pincode', 'image', 'is_donor', 'last_donated_date']

class BloodRequestSessionForm(forms.ModelForm):
    """
    This is a form class for blood request session
    """
    blood_groups = forms.MultipleChoiceField(choices = [(each, str(each.name)) for each in BloodGroup.objects.all()], widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = BloodRequestSession
        fields = ['req_user', 'pincode', 'total_unit', 'req_date','till_date', 'blood_groups']
        labels = {'req_user':'Enter name','pincode':'Enter pincode','total_unit':'Enter total_unit'}
        widgets = {'req_user': forms.HiddenInput()}
        error_messages = {
            'req_user':{'required':"Enter name"},
            'pincode':{'required':"Enter pincode"},
            'total_unit':{'required':"Enter total_unit"},
            'req_date':{'required':"Enter req_date"},
            'till_date':{'required':"Enter till_date"},
            'blood_groups':{'required':"Enter blood_group"},
        }