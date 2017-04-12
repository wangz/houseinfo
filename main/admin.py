from django.contrib import admin

# Register your models here.


from main.models import *


admin.site.register(City)  
admin.site.register(TotalPerDay)
admin.site.register(Data) 
admin.site.register(MSummary) 
