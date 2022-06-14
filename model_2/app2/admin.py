from django.contrib import admin
from app2.models import Biodata
# Register your models here.




#for showing data like in a table fomrat we need ModelAdmin class

#register using decorater
@admin.register(Biodata)
class BiodataAdmin(admin.ModelAdmin):
    list_display=('Id','name','mail','address')

# admin.site.register(Biodata,BiodataAdmin)