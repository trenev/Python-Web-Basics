from os import remove

from django import forms

from workshop_petstagram.main.helpers import BootstrapFormMixin, DisabledFieldsFormMixin, get_profile_pet_photos
from workshop_petstagram.main.models import Profile, PetPhoto, Pet


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'date_of_birth', 'email', 'gender', 'description')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Link to Profile Picture',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pet_photos = get_profile_pet_photos()
        images_path = []
        for photo in pet_photos:
            images_path.append(photo.photo.path)
            photo.delete()

        self.instance.delete()
        [remove(im_p) for im_p in images_path]

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class AddPetForm(BootstrapFormMixin,  forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
        }


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }


class AddPetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
        }


class EditPetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        labels = {
            'tagged_pets': 'Tag Pets',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
        }
