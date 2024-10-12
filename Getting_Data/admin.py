from django.contrib import admin
from Getting_Data.models import Data_Getting


class Data_Getting_data(admin.ModelAdmin):
    data=('Name','Father_Name','Mother_Name')

admin.site.register(Data_Getting,Data_Getting_data)
    
