from django import forms

from exam_recipes.web.models import Recipe


class RemoveLabelSuffixFormMixin:
    fields = {}

    def _init_remove_colons(self):
        for name, field in self.fields.items():
            field.label_suffix = ''


class DisabledFieldsFormMixin:
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            field.required = False
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['disabled'] = True


class RecipeForm(RemoveLabelSuffixFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'cooking_time': 'Time (Minutes)',
        }


class DeleteForm(RemoveLabelSuffixFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'cooking_time': 'Time (Minutes)',
        }
