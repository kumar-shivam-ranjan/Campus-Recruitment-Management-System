from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import stu_details,job_pos
from django.forms.widgets import DateInput,CheckboxSelectMultiple
from django.http import request




class Student_SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='*required')
    last_name = forms.CharField(max_length=30, required=True, help_text='*required')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1', 'password2', )
        widgets={'dob':DateInput(attrs={'type':'date'})}


class UsdForm(forms.Form):
    sop = forms.CharField(max_length=500, initial="enter ur sop",required=True)
    phone_number = forms.CharField(max_length=10,min_length=10,initial="enter ur phn num",required=True)

class dispstuForm(forms.ModelForm):
    class Meta:
        model=stu_details
        fields=('username','phone_number','fathers_name','mothers_name','gender','place','branch','cgpa_Btech','class_10_cgpa','class_12_percentage','certifications_count',\
               'internship','languages','sop','dob')


c_type = (
    ('product', 'product'),
    ('service', 'service'))


class company_SignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=30, required=True, help_text='*required')
    est_year=forms.CharField(max_length=4,required=True,help_text="*required")
    hr_name=forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn=forms.CharField(max_length=10, min_length=10,required=True, help_text='*required')
    headquaters=forms.CharField(max_length=30, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')
    type=forms.ChoiceField(required=True,choices=c_type)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'company_name', 'est_year','hr_name','hr_phn','headquaters','about','type','email','password1', 'password2', )


class ccdForm(forms.Form):
    hr_name = forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn = forms.CharField(max_length=10, min_length=10, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')


class jobposForm(forms.ModelForm):
    class Meta:
        model=job_pos
        fields=('company_name','username','job_id','designation' ,'salary'  ,'bond_years','information_technology','mech', 'civil','eee',  'ece', 'chemical' ,'cse')