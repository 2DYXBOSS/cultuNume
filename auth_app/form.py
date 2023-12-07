from  django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class AuthUser(UserCreationForm):
    
    
    email = forms.EmailField(
        label="entrer un e-mail",
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'email'}),
    )
    password1 = forms.CharField(
        label="entrer un mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )

    password2 = forms.CharField(
        label="confirmation de mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )
    # class meta pour personnaliser les chants du formulaire
    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields +("password1","password2")
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class MonFormulaireInscription(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
