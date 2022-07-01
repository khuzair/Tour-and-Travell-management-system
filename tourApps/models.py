from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


my_choices = (
    ('one', 'BT 01'),
    ('two', 'BT 02'),
    ('three', 'BT 03'),
    ('four', 'BT 04'),
    ('five', 'BT 05'),
    ('six', 'BT 06')
)

suggestion = (
    ('car', 'CAR $60 per day'),
    ('bike', 'BIKE $40 dollar per day'),
    ('small coach', 'SMALL COACH $70 per day'),
    ('coach', 'COACH $100 per day')
)
class Header(models.Model):
    title = models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=100)
    contact = models.CharField(max_length=20)
    date_time = models.DateTimeField(default=timezone.now)


class BookingTour(models.Model):
    tour_code = models.CharField(max_length=100, choices=my_choices)
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100)
    phone_no = models.DecimalField(max_digits=12, decimal_places=5)
    departure_time = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    pickup_add = models.TextField()
    drop_add = models.TextField()
    vhical_type = models.CharField(max_length=100, choices=suggestion)
    num_passenger = models.IntegerField(default=1)
    additional_msg = models.TextField()


class Horizon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Swipper(models.Model):
    img = models.ImageField(upload_to='swipper', height_field="image_height", width_field="image_width", max_length=100)
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="1920")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="678")
    description = models.TextField()
    caption = models.TextField()

class Tour(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Tour', height_field="image_height", width_field="image_width", max_length=100)
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="420")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="368")

class HotTour(models.Model):
    name = CharField(max_length=30)
    img = ImageField(upload_to='Tour', height_field="image_height", width_field="image_width", max_length=100)
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="366")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="600")
    price = IntegerField(default=0)
    description = TextField()

class CustomLoginModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)