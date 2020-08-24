
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', include('campus.urls')),
    path('student/student_register/', include('campus.urls')),
    path('student/student_login/',include('campus.urls')),
    path('student/student_login/usd/',include('campus.urls')),
    path('logout/',include('campus.urls')),
    path('student/student_login/dispstu/', include('campus.urls')),
    path('company/company_register/', include('campus.urls')),
    path('company/company_login/', include('campus.urls')),
    path('company/company_login/ccd/',include('campus.urls')),
    path('company/company_login/jp/', include('campus.urls')),
    path('company/company_login/jd/', include('campus.urls')),
    path('company/company_login/viewpos/', include('campus.urls')),
    path('student/student_login/applyjob/',include('campus.urls')),
    path('student/student_login/applyjob/<str:opt>/',include('campus.urls')),
    path('company/company_login/selectstu/', include('campus.urls')),
    path('company/company_login/selectstu/<str:opt>/',include('campus.urls')),

]