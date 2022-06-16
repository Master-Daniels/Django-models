from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author =  models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateField(default=timezone.now)
    Published_date = models.DateField(blank=True, null=True)
