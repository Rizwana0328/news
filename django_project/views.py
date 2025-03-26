from django.contrib.auth.views import PasswordResetConfirmView
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"  # Use your custom template

    def get(self, request, uidb64, token, *args, **kwargs):
        """
        This method handles GET requests for password reset confirmation.
        It ensures the reset token is valid before displaying the reset form.
        """
        try:
            uid = urlsafe_base64_decode(uidb64).decode()  # Decode user ID
            user = User.objects.get(pk=uid)

            # Check if the token is valid
            if default_token_generator.check_token(user, token):
                return super().get(request, uidb64, token, *args, **kwargs)
            else:
                return HttpResponse("Invalid or expired password reset link.", status=400)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return HttpResponse("Invalid user.", status=400)
