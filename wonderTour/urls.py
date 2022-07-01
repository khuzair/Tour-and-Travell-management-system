from django.contrib import admin
from django.urls import path, include
from tourApps import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/login',TemplateView.as_view(template_name = 'account/login.html'), name="social-login"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('booking/', views.booking, name="book-tour"),
    path('', include('tourApps.urls', namespace="tourApps")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
