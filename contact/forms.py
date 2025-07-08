from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = (
            'first_name','last_name','phone'
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            raise ValidationError( # não funciona.
                'First Name é igual a Last Name.'
            )
        if len(first_name) == 1:
            self.add_error(
                'first_name',ValidationError('First name não pode conter apenas um caracter',code='invalid')
            )
        if len(last_name) == 1:
            self.add_error(
                'last_name',ValidationError('Last name não pode conter apenas um caracter',code='invalid')
            )
        return super().clean()
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 8:
            self.add_error(
                'phone',
                ValidationError(
                    'Numero de *phone deve conter ao mínimo oito números.',
                    code='invalid'
                )
            )

        return phone
    