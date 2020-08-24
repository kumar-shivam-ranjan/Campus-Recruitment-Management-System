from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.models import User

done = (
    ('yes', 'yes'),
    ('no', 'no'),
)


class stu_details(models.Model):
    branch_choices = (
        ('it', 'information_technology'),
        ('me', 'mech'),
        ('ce', 'civil'),
        ('eee', 'eee'),
        ('ece', 'ece'),
        ('ch', 'chemical'),
        ('cse', 'cse'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
        ('others','others'))

    username=models.CharField(max_length=9,blank=False,help_text="enter username ex:y16it***",default="y1")
    name = models.CharField(max_length=30, blank=False, help_text='*required',default="full name")
    phone_number = models.CharField(validators=[MaxLengthValidator(10),MinLengthValidator(10)] ,help_text='*required',max_length=10)
    fathers_name = models.CharField(max_length=30, blank=False, help_text='*required')
    mothers_name = models.CharField(max_length=30, blank=False, help_text='*required')
    gender=models.CharField(blank=False, choices=gender,max_length=10)
    place = models.CharField(max_length=30, blank=False)
    branch = models.CharField(blank=False, choices=branch_choices, max_length=10)
    cgpa_Btech = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
    class_10_cgpa = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
    class_12_percentage = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='*required')
    certifications_count = models.IntegerField(blank=False)
    internship = models.CharField(blank=False, choices=done,max_length=10)
    languages = models.CharField(max_length=100, blank=False, help_text='*required')
    sop = models.CharField(max_length=500, default="statement of purpose", help_text='*required')
    dob = models.DateField(blank=False, help_text='*format is YYYY-MM-DD', )
    email = models.EmailField(max_length=254, blank=False, help_text='Required. Inform a valid email address.',default="anudeep.insvirat@gmail.com")

    def __str__(self):
       return self.username


class comp_details(models.Model):
    username=models.CharField(max_length=30,blank=False , help_text='*required')
    company_name = models.CharField(max_length=30, blank=False, help_text='*required')
    est_year = models.CharField(max_length=4, blank=False, help_text="*required")
    hr_name = models.CharField(max_length=30, blank=False, help_text='*required')
    hr_phn = models.CharField(max_length=10,validators=[MinValueValidator(10),MaxValueValidator(10)], blank=False, help_text='*required')
    headquaters = models.CharField(max_length=30,blank=False, help_text='*required')
    about = models.CharField(max_length=1000, blank=False, help_text='*required')
    type = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254,blank=False, help_text='Required. Inform a valid email address.')

    def __str__(self):
        return self.username

class job_pos(models.Model):
    job_id=models.CharField(max_length=30, blank=False, help_text='*required',unique=True)
    username = models.CharField(max_length=30, blank=False, help_text='*required')
    company_name = models.CharField(max_length=30, blank=False, help_text='*required')
    designation = models.CharField(max_length=30, blank=False, help_text='*required')
    salary=models.IntegerField( blank=False, help_text='*required')
    bond_years=models.IntegerField( blank=False, help_text='*required')
    information_technology= models.CharField(blank=False, choices=done, max_length=10)
    mech= models.CharField(blank=False, choices=done, max_length=10)
    civil= models.CharField(blank=False, choices=done, max_length=10)
    eee = models.CharField(blank=False, choices=done, max_length=10)
    ece= models.CharField(blank=False, choices=done, max_length=10)
    chemical= models.CharField(blank=False, choices=done, max_length=10)
    cse= models.CharField(blank=False, choices=done, max_length=10)

    def __str__(self):
        return self.job_id


class applied_jobs(models.Model):
    company_id = models.CharField(max_length=30, blank=False, help_text='*required' ,default="company id")
    job_id = models.CharField(max_length=30, blank=False, help_text='*required',default="job id")
    student_id= models.CharField(max_length=9, blank=False, help_text="enter username ex:y16it***", default="y1")

    def __str__(self):
        return self.job_id

