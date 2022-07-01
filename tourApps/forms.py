from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import fields
from .models import BookingTour
from .models import CustomLoginModel
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import SetPasswordField
from allauth.account import app_settings
from allauth.account.utils import user_field, user_email, user_username
from django.utils.translation import ugettext_lazy as _
from allauth.account.adapter import get_adapter


class SocialPasswordedSignupForm(SignupForm):

    password1 = SetPasswordField(label=_("Password"))
    password2 = SetPasswordField(label=_("Confirm Password"))

    def __init__(self, *args, **kwargs):
        self.sociallogin = kwargs.pop('sociallogin')
        user = self.sociallogin.user
        # TODO: Should become more generic, not listing
        # a few fixed properties.
        initial = {'email': user_email(user) or '',
                   'username': user_username(user) or '',
                   'first_name': user_field(user, 'first_name') or '',
                   'last_name': user_field(user, 'last_name') or ''}
        kwargs.update({
            'initial': initial,
            'email_required': kwargs.get('email_required',
                                         app_settings.EMAIL_REQUIRED)})
        super(SocialPasswordedSignupForm, self).__init__(*args, **kwargs)

    def save(self, request):
        adapter = get_adapter()
        user = adapter.save_user(request, self.sociallogin, form=self)
        self.custom_signup(request, user)
        return user

    def clean(self):
        super(SocialPasswordedSignupForm, self).clean()
        if "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                raise forms.ValidationError(_("You must type the same password"
                                              " each time."))

    def raise_duplicate_email_error(self):
        raise forms.ValidationError(
            _("An account already exists with this e-mail address."
              " Please sign in to that account first, then connect"
              " your %s account.")
            % self.sociallogin.account.get_provider().name)

    def custom_signup(self, request, user):
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.save()


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields['password'].widget.attrs.update({
            "id": "password-field",
            "type": "password",
            "class": "form-control",
            "placeholder": "Password"
        })
    class Meta:
        model = CustomLoginModel
        fields = '__all__'

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'input id': 'username',
            'type': 'text',
            'name': 'username',
            'placeholder': 'Username',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['first_name'].widget.attrs.update({
            'input id': 'firstName',
            'type': 'text',
            'name': 'firstname',
            'placeholder': 'First Name',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['last_name'].widget.attrs.update({
            'input id': 'lastName',
            'type': 'text',
            'name': 'lastname',
            'placeholder': 'Last Name',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['email'].widget.attrs.update({
            'input id': 'email',
            'type': 'email',
            'name': 'email',
            'placeholder': 'Email Address',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['password1'].widget.attrs.update({
            'input id': 'password',
            'type': 'password',
            'name': 'password',
            'placeholder': 'Password',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['password2'].widget.attrs.update({
            'input id': 'passwordConfirmation',
            'type': 'password',
            'name': 'passwordConfirmation',
            'placeholder': 'Confirm Password',
            'class': "form-control bg-white border-left-0 border-md"
        })
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingTour
        fields = '__all__'