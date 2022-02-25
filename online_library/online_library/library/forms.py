from django import forms

from online_library.library.models import Profile, Book


class RemoveLabelSuffixMixin:
    fields = {}

    def _init_remove_colons(self):
        for _, field in self.fields.items():
            field.label_suffix = ''


class ProfileForm(RemoveLabelSuffixMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Image URL',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'profile_image': forms.TextInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        Book.objects.all().delete()
        self.instance.delete()
        return self.instance


class BookForm(RemoveLabelSuffixMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_remove_colons()

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'book_image': 'Image',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'rows': 3,
                }
            ),
            'book_image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            ),
        }


class CreateBookForm(BookForm):
    pass


class EditBookForm(BookForm):
    pass
