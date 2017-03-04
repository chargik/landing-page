from django import forms
from .models import Join


class JoinForm(forms.ModelForm):
    email = forms.EmailField(label='',
            widget=forms.EmailInput(
                    attrs={
                        'placeholder':'Your email',
                        'class':'form-control sign-up-email-form'
                        }
                ))
    class Meta:
        model = Join
        fields = ['email']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        qs = Join.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email already exist")
        return email