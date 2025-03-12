from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # This is the model we are using for the form
        fields = (
            "username",
            "email",
            "age",
        )  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser  
        fields = (
            "username",
            "email",
            "age",
        )


