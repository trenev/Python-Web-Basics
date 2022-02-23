from django import forms

from task_manager.tasks.models import Task


class RemoveLabelSuffixFormMixin:
    fields = {}

    def _init_remove_colons(self):
        for name, field in self.fields.items():
            field.label_suffix = ''


class TaskForm(RemoveLabelSuffixFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()

    class Meta:
        model = Task
        fields = ('title', 'description', 'dead_line')

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
            'dead_line': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
        }
