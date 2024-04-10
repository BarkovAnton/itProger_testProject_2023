from django import forms
from .models import UsersUrls


class UrlsAddForm(forms.ModelForm):

    url_large = forms.URLField(
        label='Длинная ссылка', 
        required=True,
        help_text='Введите ссылку. Длина ссылки не более 100 сиволов',
        widget=forms.TextInput(attrs={
            'class': 'reg-field', 
        })
    )

    url_small = forms.CharField(
        label='Сокращенная ссылка', 
        required=True,
        help_text='Введите слово сокращение. Длина не более 20 сиволов',
        widget=forms.TextInput(attrs={
            'class': 'reg-field', 
        })
    )

    class Meta:
        model = UsersUrls
        fields = ['url_large', 'url_small']