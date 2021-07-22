from django.contrib import admin

# Register your models here.

from .models import SocialLink, Entity, School, DiplomaAward, Experience

admin.site.register(SocialLink)
admin.site.register(Entity)
admin.site.register(School)
admin.site.register(DiplomaAward)
admin.site.register(Experience)