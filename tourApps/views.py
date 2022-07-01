from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Header, Tour, Swipper, HotTour, Horizon
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, BookingForm, CustomLoginForm


def booking(request):
  
    return render(request, 'registrations/booking_tour.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'the new user {username} has been created')
                return redirect('login')

        context = {
            "form": form
        }
        return render(request, 'registrations/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = CustomLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_pswd = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_pswd)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form  = CustomLoginForm()
        return render(request, 'registrations/login.html', {"form": form})

def logoutPage(request):
    logout(request)
    return redirect('/')

class IndexListView(generic.ListView):
    template_name = "index.html"
    queryset = Header.objects.get()
    context_object_name = "header"
    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['Tour'] = Tour.objects.all()
        context['Swipper'] = Swipper.objects.all()
        context['HotTour'] = HotTour.objects.all()
        context['Horizon'] = Horizon.objects.all()
        return context

class AboutListView(generic.ListView):
    template_name = "about.html"
    context_object_name = "header"
    def get_queryset(self):
        queryset = Header.objects.get()
        return queryset
    
 

class TypographyListView(generic.ListView):
    template_name = "typography.html"
    context_object_name = "header"
    def get_queryset(self):
        queryset = Header.objects.get()
        return queryset


class ContactListView(generic.ListView):
    template_name = "contact-us.html"
    context_object_name = "header"
    def get_queryset(self):
        queryset = Header.objects.get()
        return queryset
