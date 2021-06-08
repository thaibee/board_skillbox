from django import forms
from django.core.exceptions import ValidationError

from advers.models import Owner, Adver


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['l_name', 'f_name', 'phone_number', 'email', 'birthday']

    birthday = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',)
    )


class AdverForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=20)
    description = forms.CharField(min_length=10, max_length=20)
    price = forms.IntegerField(min_value=10, max_value=10000)

    def clean_title(self):
        data = self.cleaned_data['title']
        if data == 'туй':
            raise ValidationError('Нельзя продавать туй')
        return data

    def clean(self):
        cleaned_data = super(AdverForm, self).clean()
        price = cleaned_data['price']
        if price == 11:
            msg = 'Смешная цена'
            self.add_error('price', msg)
