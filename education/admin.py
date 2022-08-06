from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
from .models import *
from .forms import ApplicationForm

class ApplicationAdmin(admin.ModelAdmin):
    list_display =['first_name', 'other_names', 'studytime', 'level', 'gender', 'campus', 'courses', 'Date_of_birth', 'email',
    'phone', 'residence', 'nationality', 'where', 'file1', 'file2', 'file3', 'other_contact' ]
    form = ApplicationForm
    list_filter = ['other_names', 'campus']
# Register your models here.
admin.site.register(Application)
admin.site.register(Course)
=======

# Register your models here.
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
=======

# Register your models here.
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
