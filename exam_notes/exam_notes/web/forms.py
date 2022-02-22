from django import forms

from exam_notes.web.models import Profile, Note


class RemoveLabelSuffixFormMixin:
    fields = {}

    def _init_remove_colons(self):
        for _, field in self.fields.items():
            field.label_suffix = ''


class ProfileForm(RemoveLabelSuffixFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()

    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    pass


class NoteForm(RemoveLabelSuffixFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()

    class Meta:
        model = Note
        fields = '__all__'


class CreateNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
