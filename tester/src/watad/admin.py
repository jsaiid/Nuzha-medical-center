from django.contrib import admin
from watad.models import *
from django.utils.html import format_html


# Register your models here.
class activities_admin(admin.ModelAdmin):
    list_display=['id','img','title','desc','date']  
    def img(self,obj):
        return format_html('<img src="{}" width="100px"',obj.image.url)
    

class partners_admin(admin.ModelAdmin):
    list_display=['id','img','name']  
    def img(self,obj):
        return format_html('<img src="{}" width="100px"',obj.image.url)
    
class activity_admin(admin.ModelAdmin):
    list_display=['id','name','date','exp_date','email','phone','about_watad','proj_title','desc','training_prog','proj_length','quotation_currency','how_to_apply','note']  
    def img(self,obj):
        return format_html('<img src="{}" width="100px"',obj.image.url)
    

class contact_admin(admin.ModelAdmin):
    list_display=['id','name','email','phone','subject','message']  

    
class details_job_admin(admin.ModelAdmin):
    list_display=['id','image','title','desc','date']  
    def img(self,obj):
        return format_html('<img src="{}" width="100px"',obj.image.url)

class calls_admin(admin.ModelAdmin):
    list_display=['id','name','date','exp_date','email','phone']
    




admin.site.register(activities, activities_admin)
admin.site.register(partners, partners_admin)
admin.site.register(contact, contact_admin)
admin.site.register(activity, activity_admin)
admin.site.register(details_job, details_job_admin)

admin.site.register(calls, calls_admin)

