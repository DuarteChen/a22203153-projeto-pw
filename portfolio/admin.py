from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
from .models import Videos

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)


admin.site.register(ScientificArea)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(Subject)
admin.site.register(Concept)


