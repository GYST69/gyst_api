
from django.contrib.auth.models import User

# Create your models here.

class Account(User):
    USERNAME_FIELD = 'email'

