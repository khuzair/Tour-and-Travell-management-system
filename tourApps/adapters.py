from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from allauth.exceptions import ImmediateHttpResponse
from django.contrib.auth import get_user_model
from allauth.account.utils import perform_login
from django.http import response
User = get_user_model()


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # This isn't tested, but should work
        try:
            user = User.objects.get(email=sociallogin.email)
            sociallogin.connect(request, user)
            # Create a response object
            raise ImmediateHttpResponse(response)
        except User.DoesNotExist:
            pass
            
    def is_open_for_signup(self, request, sociallogin):        
        return True

class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):


    def pre_social_login(self, request, sociallogin):
        try:
            get_user_model().objects.get(email=sociallogin.user.email)
        except get_user_model().DoesNotExist:
            from django.contrib import messages
            messages.add_message(request, messages.ERROR, 'Social logon from this account not allowed.') 
            raise ImmediateHttpResponse(HttpResponse(status=500))
        else:
            user = get_user_model().objects.get(email=sociallogin.user.email)
            if not sociallogin.is_existing:
                sociallogin.connect(request, user) 

    def is_open_for_signup(self, request, sociallogin):        
        return True