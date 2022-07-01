from django.urls import path
from .views import IndexListView, AboutListView, TypographyListView, ContactListView

app_name = 'tourApps'

urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('about/', AboutListView.as_view(), name="about"),
    path('typography/', TypographyListView.as_view(), name="typography"),
    path('contact/', ContactListView.as_view(), name="contact"),
]
