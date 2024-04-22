from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=254)
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"

        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        # Add custom password validation rules here if needed

        return cleaned_data