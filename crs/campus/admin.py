from django.contrib import admin
from campus.models import stu_details,comp_details,job_pos,applied_jobs
admin.site.register(stu_details)
admin.site.register(comp_details)
admin.site.register(job_pos)
admin.site.register(applied_jobs)