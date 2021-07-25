from django.contrib import admin

# Register your models here.

from .models import SocialLink, Entity, School, DiplomaAward, Experience, GeneralConfig, Interest, Project

admin.site.register(SocialLink)
admin.site.register(Entity)
admin.site.register(School)
admin.site.register(DiplomaAward)
admin.site.register(Experience)
admin.site.register(GeneralConfig)
admin.site.register(Interest)
admin.site.register(Project)