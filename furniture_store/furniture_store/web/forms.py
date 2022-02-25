from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from furniture_store.web.validators import validate_min_price


class FurnitureForm(forms.Form):
    type = forms.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(4),
        ),
        widget=forms.TextInput(
            attrs={'class': 'form-control valid'},
        ),
    )

    price = forms.FloatField(
        validators=(
            validate_min_price,
        ),
        widget=forms.NumberInput(
            attrs={'class': 'form-control'},
        ),
    )

    model = forms.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(4),
        ),
        widget=forms.TextInput(
            attrs={'class': 'form-control is-valid'},
        ),
    )

    image = forms.URLField(
        widget=forms.URLInput(
            attrs={'class': 'form-control'},
        ),
    )

    year = forms.IntegerField(
        validators=(
            MinValueValidator(1950),
            MaxValueValidator(2050),
        ),
        widget=forms.NumberInput(
            attrs={'class': 'form-control is-invalid'},
        ),
    )

    material = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        ),
        # null=True,
        # blank=True,
    )

    description = forms.CharField(
        max_length=100,
        validators=(
            MinLengthValidator(10),
        ),
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        ),
    )


class CreateFurnitureForm(FurnitureForm):
    pass


class EditFurnitureForm(FurnitureForm):
    pass
