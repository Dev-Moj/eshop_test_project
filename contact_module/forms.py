from django import forms
from .models import contactUs


class contactUsforms(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            'max_length': 'تعداد کاراکتر ها نمیتواند بیشتر از ۵۰ کاراکتر باشد',
            'required': 'این فیلد باید پر شود'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    emile = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'ایمیل'

        }))
    title = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'موضوع'
        }
        ))
    message = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={
            'id': 'message',
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'پیغـام شمـا',
            'rows': '8'
        }
        ))


class contactUsModelForms(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['title', 'full_name', 'message', 'emile']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'emile': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'موضوع'
            }),
            'message' : forms.Textarea(attrs={
                'id': 'message',
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'پیغـام شمـا',
                'rows': '8'
            }
            )

        }
