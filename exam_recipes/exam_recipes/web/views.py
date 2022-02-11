from django.shortcuts import render, redirect

from exam_recipes.web.forms import RecipeForm, DeleteForm
from exam_recipes.web.models import Recipe


def get_all_recipes():
    return Recipe.objects.all()


def get_recipe(pk):
    return Recipe.objects.get(pk=pk)


def show_home(request):
    context = {
        'recipes': get_all_recipes(),
    }

    return render(request, 'index.html', context)


def recipe_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'recipe': instance,
    }

    return render(request, template_name, context)


def create_recipe(request):
    return recipe_action(request, RecipeForm, 'index', Recipe(), 'create.html')


def edit_recipe(request, pk):
    return recipe_action(request, RecipeForm, 'index', get_recipe(pk), 'edit.html')


def delete_recipe(request, pk):
    return recipe_action(request, DeleteForm, 'index', get_recipe(pk), 'delete.html')


def show_details_recipe(request, pk):
    recipe = get_recipe(pk)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(','),
    }

    return render(request, 'details.html', context)
