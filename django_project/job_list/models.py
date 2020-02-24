from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import timedelta

def expire_date(offset):
    return timezone.now() + timedelta(days=offset)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_expire = models.DateField(default=expire_date(30))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sallary = models.CharField(default='Negociabil', max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})