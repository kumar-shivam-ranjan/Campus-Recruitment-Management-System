from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Student_SignUpForm,UsdForm,dispstuForm,company_SignUpForm,ccdForm,jobposForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from campus.models import stu_details,comp_details,job_pos,applied_jobs
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

# Create your views here
def  student_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='student').exists():
        return render(request,'campus/stulog.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.groups.filter(name='student').exists():
             return render(request, 'campus/stulog.html', {'form': form})
            else:
                logout(request)
                return render(request, 'campus/student_login.html', {'form': form})
        else:
            return render(request, 'campus/student_login.html', {'form': form})


    else:
        form = AuthenticationForm()
        return render(request, 'campus/student_login.html', {'form': form})

def  home(request):
    return render(request,'campus/home.html')

def pagelogout(request):
        logout(request)

        return redirect('http://127.0.0.1:8000/')


def student_register(request):
    if request.method == 'POST':
        form = Student_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/student/student_login/')

        else:
            return render(request, 'campus/register.html', {'form': form})
    else:
        form =Student_SignUpForm()
        return render(request, 'campus/register.html', {'form': form})

#@login_required
#@user_passes_test(lambda u: u.groups.filter(name='Student').count() == 1)
def usd(request):
 if  request.user.is_authenticated and request.user.groups.filter(name='student').exists():
    if request.method == "POST":
            form=UsdForm(request.POST)
            if form.is_valid():
                stu = request.user.username
                post = stu_details.objects.filter(username=stu)
                x= request.POST.get('sop')
                y=request.POST.get('phone_number')
                db=request.POST.get('dob')
                e=request.POST.get('email')
                l=request.POST.get('languages') 
                cc=request.POST.get('certifications_count')
                i=request.POST.get('internship')
                c12=request.POST.get('class_12_percentage')
                c10=request.POST.get('class_10_cgpa')
                b=request.POST.get('branch')
                cb=request.POST.get('cgpa_Btech')
                p=request.POST.get('place')
                g=request.POST.get('gender')
                fn=request.POST.get('fathers_name')
                mn=request.POST.get('mothers_name')
                name=request.POST.get('name')

                j=post[0]
                j.sop =x
                j.phone_number = y
                j.dob=db
                j.email=e
                j.languages=l
                j.certifications_count=cc
                j.internship=i
                j.class_12_percentage=c12
                j.class_10_cgpa=c10
                j.branch=b
                j.cgpa_Btech=cb
                j.place=p
                j.gender=g
                j.fathers_name=fn
                j.mothers_name=mn
                j.name=name
                j.save()
                return render(request, 'campus/stulog.html')

    else:
        stu = request.user.username
        post = stu_details.objects.filter(username=stu)
        x = post[0].sop
        x=str(x)
        y = post[0].phone_number
        print(x,y,post)
        form=UsdForm()
        db=post[0].dob
        e=post[0].email
        l=post[0].languages 
        cc=post[0].certifications_count
        i=post[0].internship
        c12=post[0].class_12_percentage
        c10=post[0].class_10_cgpa
        b=post[0].branch
        cb=post[0].cgpa_Btech
        p=post[0].place
        g=post[0].gender
        fn=post[0].fathers_name
        mn=post[0].mothers_name
        name=post[0].name
        context={'form': form,'x':x,'y':y,'db': db,"e":e,"l":l,"cc":cc,"i":i,"c12":c12,"c10":c10,"b":b,"cb":cb,"p":p,"g":g,"fn":fn,"mn":mn,"name":name}
        return render(request, 'campus/usd.html',context)
 else:
     return HttpResponse("<h1>u r not logged in</h1>")



def dispstu(request):
    if request.user.is_authenticated and request.user.groups.filter(name='student').exists():
        stu = request.user.username
        post = stu_details.objects.filter(username=stu)
        form=dispstuForm()
        return render(request, 'campus/dispstu.html', {'form': form, 'post': post})
    else:
        return HttpResponse("<h1>u r not logged in</h1>")



def company_register(request):
    if request.method == 'POST':
        form = company_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='company')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            a=comp_details()
            a.username=request.POST.get('username')
            a.company_name=request.POST.get('company_name')
            a.email=request.POST.get('email')
            a.est_year=request.POST.get('est_year')
            a.type=request.POST.get('type')
            a.about=request.POST.get('about')
            a.hr_name=request.POST.get('hr_name')
            a.hr_phn=request.POST.get('hr_phn')
            a.headquaters=request.POST.get('headquaters')
            a.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'campus/register1.html', {'form': form})

    else:
        form =company_SignUpForm()
        return render(request, 'campus/register1.html', {'form': form})



def  company_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        return render(request,'campus/comlog.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.groups.filter(name='company').exists():
             return render(request, 'campus/comlog.html', {'form': form})
            else:
                logout(request)
                return render(request, 'campus/company_login.html', {'form': form})
        else:
            return render(request, 'campus/company_login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'campus/company_login.html', {'form': form})




def ccd(request):
 if  request.user.is_authenticated and request.user.groups.filter(name='company').exists():
    if request.method == "POST":
            form=ccdForm(request.POST)
            if form.is_valid():
                stu = request.user.username
                post = comp_details.objects.filter(username=stu)
                x= request.POST.get('hr_name')
                y=request.POST.get('hr_phn')
                z=request.POST.get('about')
                j=post[0]
                j.hr_name =x
                j.hr_phn = y
                j.about=z
                j.save()
                return render(request, 'campus/comlog.html')

    else:
        stu = request.user.username
        post = comp_details.objects.filter(username=stu)
        x = post[0].hr_name
        x=str(x)
        y = post[0].hr_phn
        z=post[0].about
        form=ccdForm()
        return render(request, 'campus/ccd.html', {'form': form,'x':x,'y':y,'z':z})
 else:
     return HttpResponse("<h1>u r not logged in</h1>")



def jobpos(request):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        if request.method == "POST":
            form = jobposForm(request.POST)
            if form.is_valid():
                    model_instance = form.save(commit=False)
                    model_instance.save()
                    return render(request,'campus/comlog.html')
            else:
                return render(request, 'campus/jobpos.html', {'form': form})
        else:
            form = jobposForm()
            x = request.user.username
            y = comp_details.objects.filter(username=x)
            y = str(y[0].company_name)
            y=y.split()
            y1=""
            for i in y:
                y1=y1+"_"+i
            y1=y1[1:len(y1)]
            print(y)

            return render(request, 'campus/jobpos.html', {'form': form,'x':x,'y':y1})
    else:
        return HttpResponse("<h1>u r not logged in</h1>")

def jd(request):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        if request.method == "POST":
                    s=""
                    print("hiiiiiii")
                    book=job_pos.objects.filter(job_id=request.POST.get("job_id"))
                    print(len(book))
                    if(len(book)!=1):
                        s="wrong job id try again"
                        return render(request, 'campus/jd.html',{'s':s})
                    book=book[0]
                    book.designation=request.POST.get("designation")
                    book.salary=request.POST.get("salary")
                    book.bond_years=request.POST.get("bond_years")
                    book.information_technology=request.POST.get("information_technology")
                    book.mech=request.POST.get("mech")
                    book.civil=request.POST.get("civil")
                    book.ece=request.POST.get("ece")
                    book.eee=request.POST.get("eee")
                    book.chemical=request.POST.get("chemical")
                    book.cse=request.POST.get("cse")
                    book.save()
                    return render(request,'campus/comlog.html',{'s':s})


        else:
            x = request.user.username
            y = comp_details.objects.filter(username=x)
            y = str(y[0].company_name)
            y=y.split()
            y1=""
            for i in y:
                y1=y1+"_"+i
            y1=y1[1:len(y1)]

            return render(request, 'campus/jd.html', {'x':x,'y':y1})
    else:
        return HttpResponse("<h1>u r not logged in</h1>")


def deletevacan(request):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        if request.method == "POST":
                    s=""
                    book=job_pos.objects.filter(job_id=request.POST.get("jobid"))
                    print(len(book))
                    if(len(book)!=1):
                        s="wrong job id try again"
                        return render(request, 'campus/jobdelete.html',{'s':s})
                    applied_jobs.objects.filter(job_id=book[0]).delete()
                    book[0].delete()
                    s="deleted succssefully"
                    return render(request,'campus/comlog.html',{'s':s})


        else:

            return render(request, 'campus/jobdelete.html')
    else:
        return HttpResponse("<h1>u r not logged in</h1>")

def viewpos(request):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        x = request.user.username
        y = job_pos.objects.filter(username=x)
        s=""
        print(y)
        if(len(y)==0):
            s="no vacancies posted"
        return render(request, 'campus/viewpos.html',{'y':y,'s':s})
    else:
        return HttpResponse("<h1>u r not logged in</h1>")



def applyjob(request):
    if request.user.is_authenticated and request.user.groups.filter(name='student').exists():
      s=""
      y=[]
      if request.method == "POST":
        print("hi")
        sal=request.POST.get("salary")
        bon=request.POST.get("years")
        x = request.user.username
        b = stu_details.objects.filter(username=x)
        b = str(b[0].branch)
        print(sal,bon,b)
        if(b=="it"):
         y = job_pos.objects.filter(salary__gte=sal,bond_years__lte=bon,information_technology="yes").order_by('salary')
        if (b == "cse"):
            y = job_pos.objects.filter(salary__gte=sal, bond_years__lte=bon,cse="yes").order_by('salary')
        if (b == "me"):
            y = job_pos.objects.filter(salary__gte=sal, bond_years__lte=bon,mech="yes").order_by('salary')
        if (b == "ce"):
            y = job_pos.objects.filter(salary__gte=sal, bond_years__lte=bon,civil="yes").order_by('salary')
        if (b == "eee"):
            y = job_pos.objects.filter(salary__gte=sal, bond_years__lte=bon,eee="yes").order_by('salary')
        if (b == "ece"):
            y = job_pos.objects.filter(salary__gte=sal, bond_years__lte=bon,ece="yes").order_by('salary')
        if (b == "ch"):
            y = job_pos.objects.filter(salary__gte=sal, bond_years__lte=bon,chemical="yes").order_by('salary')
        print(y)
        if(len(y)==0):
            s="no vacancies for this preference"
            print("failed",s)
            return render(request, 'campus/applyjob.html',{'s':s})
        else:
            return render(request, 'campus/applyjob.html', {'y': y, 's': s})
      else:
          return render(request, 'campus/applyjob.html', { 'y':y,'s': s})
    else:
        return HttpResponse("<h1>u r not logged in</h1>")


def apply(request,opt):
    if request.user.is_authenticated and request.user.groups.filter(name='student').exists():
        if request.method=="POST":
            x=request.user.username
            print(x)
            y=job_pos.objects.filter(job_id=opt)[0].username
            job=applied_jobs()
            job.student_id=x
            job.company_id=y
            job.job_id=opt
            job.save()
            return HttpResponse("<h1>you have applied succesfully... all the best</h1>")


        else:
            c=job_pos.objects.filter(job_id=opt)[0].username
            print(c)
            x=comp_details.objects.filter(username=c)
            print(x)
            return render(request,'campus/compdisp.html',{'post':x[0]})

    else:
        return HttpResponse("<h1>u r not logged in</h1>")


def selectstu(request):
    y=[]
    s=""
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        if request.method == "POST":
             jobid=request.POST.get("jobid")
             u=request.user.username
             x=len(job_pos.objects.filter(job_id=jobid,username=u))
             if(x==0):
                 s="enter correct job id"
                 return render(request, 'campus/sstu.html', {'y': y,'s':s})
             x=len(applied_jobs.objects.filter(job_id=jobid,company_id=u))
             if(x==0):
                s = "sorry no one applied"
                return render(request, 'campus/sstu.html', {'y': y, 's': s})
             tenth=request.POST.get("tenth")
             twth=request.POST.get("twth")
             btech=request.POST.get("btech")
             x = applied_jobs.objects.filter(job_id=jobid,company_id=u).values('student_id')
             y=[]
             print(x)
             y=[]
             print("the total number is",len(y))
             for i in x:
                 b=stu_details.objects.filter(class_10_cgpa__gte=tenth,class_12_percentage__gte=twth,cgpa_Btech__gte=btech,username=i['student_id'])
                 if(b.count()>0):
                   y.append(b)
             print("the total number is",len(y))
             if(len(y)==0):
                 s = "requirements not satisfied"
                 return render(request, 'campus/sstu.html', {'y': y, 's': s})
             else:
                 print(y)
                 return render(request, 'campus/sstu.html', {'y': y, 's': s})


        else:
          return render(request, 'campus/sstu.html', {'y': y})

    else:
        return HttpResponse("<h1>u r not logged in</h1>")


def stumail(request,opt):
    if request.user.is_authenticated and request.user.groups.filter(name='company').exists():
        if request.method=="POST":
            recv=stu_details.objects.filter(username=opt)[0].email
            name=stu_details.objects.filter(username=opt)[0].name
            p=request.user.username
            p=comp_details.objects.filter(username=p)[0].company_name
            print(recv,p)
            subject="call letter from "+p
            body="Congratlations!!!"+str(name)+" you are selected for the interview ,the date for the interview will be anounced by your Placement Officer"
            email = EmailMessage(subject, body, to=[recv])
            email.send()

            return HttpResponse("<h1>mail sent </h1>")


        else:
            print("hiiiii")
            x=stu_details.objects.filter(username=opt)
            print(x)
            return render(request,'campus/showstudent.html',{'post':x[0]})

    else:
        return HttpResponse("<h1>u r not logged in</h1>")

