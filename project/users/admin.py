from django.contrib import admin

from users.models import Citizen, Passport, UserProfile, Post

admin.site.register(Citizen)
admin.site.register(Passport)
admin.site.register(UserProfile)
admin.site.register(Post)
