from django.contrib import admin

from workshop_petstagram.main.models import Profile, Pet, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInlineAdmin,)
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'email', 'gender')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'date_of_birth', 'user_profile')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
