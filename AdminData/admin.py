from django.contrib import admin
from AdminData.models import Admin_panel

class Admin_panel_Data(admin.ModelAdmin):
    list_display=('Name','Reason','Descrption','img')



admin.site.register(Admin_panel,Admin_panel_Data)

# Register your models here.
