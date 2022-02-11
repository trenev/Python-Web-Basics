from django.contrib import admin

from exam_recipes.web.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'cooking_time')

