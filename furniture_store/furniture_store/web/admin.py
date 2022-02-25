from django.contrib import admin

from furniture_store.web.models import Profile, Furniture


class FurnitureInlineAdmin(admin.StackedInline):
    model = Furniture


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    pass
