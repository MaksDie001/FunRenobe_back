from django.contrib import admin
from .models import *
class Renobe_admin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("renobe_name",)}

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Tags)
admin.site.register(Renobe_chapters)
admin.site.register(Renobe,Renobe_admin)
admin.site.register(Counrty)
