from django.contrib import admin

from my_music_app.web.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class BookAdmin(admin.ModelAdmin):
    pass
