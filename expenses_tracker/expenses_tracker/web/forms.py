from os import remove

from django import forms
from django.core.exceptions import ValidationError

from expenses_tracker.web.models import Profile, Expense
from expenses_tracker.web.helpers import get_profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image',
        }


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if self.instance.profile_image:
            image_path = self.instance.profile_image.path
            remove(image_path)
        Expense.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image',
        }


class CreateExpenseForm(ExpenseForm):
    def clean_price(self):
        budget_left = get_profile().budget_left
        price = float(self.cleaned_data['price'])
        print(budget_left)
        print(price)
        if budget_left < price:
            raise ValidationError('Not enough budget!')
        return price


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

