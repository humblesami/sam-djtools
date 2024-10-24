from django.contrib import admin
from .models import Model1
from sam_tools.dj import DjangoUtils
from sam_tools.py import DateUtils


class Model1Admin(admin.ModelAdmin):
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        print('\nsite url = '+ DjangoUtils.site_url(request))
        print('Time = '+ DateUtils.now_str()+'\n')
        return super().render_change_form(request, context, add=False, change=False, form_url='', obj=None)


# Register your models here.
admin.site.register(Model1, Model1Admin)
