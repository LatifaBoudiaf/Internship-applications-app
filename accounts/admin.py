from django.contrib import admin
# Register your models here.

from .models import *

admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Company)
admin.site.register(InternshipApplication)
admin.site.register(internshipOffer)
admin.site.register(Marks)
admin.site.register(Presence)
admin.site.register(Notification)
admin.site.register(Certificate)
admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Admin)
