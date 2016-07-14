from django import forms

class LoginForm(forms.ModelForm):

    class Meta:
        fields = ('title', 'body', 'content')
