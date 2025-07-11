from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cada field é um widget (pelo que entendi) e isto é manipulação de widgets
        # Existe a alternativa de criar a widget para o field.
        self.fields['first_name'].widget.attrs.update({
            'class': '1234'
        })
        self.fields['phone'].widget.attrs.update({
            'minlength': '8'
        })
        self.fields['first_name'].label = 'Primeiro Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['phone'].label = 'Telefone'
        self.fields['phone'].help_text = 'Apenas telefones brasileiros.'

    class Meta():
        model = Contact
        fields = (
            'first_name','last_name','description','phone','category',
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            raise ValidationError( # não funciona.
                f'First Name é igual a Last Name.'
            )
        if len(first_name) == 1:
            self.add_error(
                'first_name',ValidationError(f'{self['first_name'].label} não pode conter apenas um caracter',code='invalid')
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
    