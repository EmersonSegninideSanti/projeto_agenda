from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
    )

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
        self.fields['category'].label = 'Categoria'
        self.fields['picture'].label = 'Imagem'
        self.fields['phone'].help_text = 'Apenas telefones brasileiros.'
        self.fields['picture'].required = False

    class Meta():
        model = Contact
        fields = (
            'first_name','last_name','description','phone','category','picture'
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
                'first_name',ValidationError(f'{self["first_name"].label} não pode conter apenas um caracter',code='invalid')
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
    
class RegisterForm(UserCreationForm):
# A validação deste *form não funciona. Muito estranho.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['first_name'].label = 'Primeiro nome'
        self.fields['last_name'].label = 'Sobrenome'

    first_name = forms.CharField(
        required=True
    )
    last_name = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        required=True
    )


    class Meta():
        model = User
        fields = (
            'username', 'email', 'password1',
            'password2', 'first_name', 'last_name'
        )

    def clean_email(self):
        email_ = self.cleaned_data.get('email')
        if User.objects.filter(email=email_).exists():
            print(User.objects.get(email = email_))
            print('Encontrou um email igual')
            # self.add_error(
            #     'email',
            #     ValidationError('Já existe este e-mail', code='invalid')
            # )
            raise ValidationError('Já existe este e-mail', code='invalid')
        return email_
    
class UpdateRegisterForm (forms.ModelForm):
# Não tem as senhas. Precisarei rever a aula.
    class Meta():
        model = User
        fields = (
            'username', 'email',
            'first_name', 'last_name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['first_name'].label = 'Primeiro nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['email'].label = 'Endereço de e-mail'