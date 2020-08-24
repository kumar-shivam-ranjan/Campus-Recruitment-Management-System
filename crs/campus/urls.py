from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('student/student_register/' , views.student_register , name='student_register'),
    path('student/student_login/', views.student_login,name='student_login'),
    path('student/student_login/usd/',views.usd,name='usd'),
    path('logout/', views.pagelogout, name='logout'),
    path('student/student_login/dispstu/',views.dispstu,name='dispstu'),
    path('company/company_register/', views.company_register, name='company_register'),
    path('company/company_login/', views.company_login, name='company_login'),
    path('company/company_login/ccd/', views.ccd, name='ccd'),
    path('company/company_login/jp/', views.jobpos, name='jp'),
    path('company/company_login/jd/', views.jd, name='jd'),
    path('company/company_login/deletevacan/', views.deletevacan, name='deletevacn'),
    path('company/company_login/viewpos/', views.viewpos, name='viewpos'),
    path('student/student_login/applyjob/', views.applyjob, name='apply'),
    path('student/student_login/applyjob/<str:opt>/', views.apply, name='apply1'),
    path('', views.home, name='home'),
    path('company/company_login/selectstu/', views.selectstu, name='sstu'),
    path('company/company_login/selectstu/<str:opt>/',views.stumail,name="sm")
    

]
