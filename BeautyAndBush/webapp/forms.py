from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=254, help_text="Required. Must be a valid email address.")

    class Meta:
        model = User
        fields = ("email", "password1", "password2")  # Include additional fields if needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"  # Change label for username field
        self.fields["password1"].label = "Password"  # Change label for password1 field
        self.fields["password2"].label = "Confirm Password"  # Change label for password2 field