from django.contrib import admin
from .models import VideoComment, categorylist,Item
from embed_video.admin import AdminVideoMixin
# Register your models here.
class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass

admin.site.register(categorylist)
admin.site.register(Item,MyModelAdmin)
admin.site.register(VideoComment)

