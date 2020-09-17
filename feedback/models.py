from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class FeedBack(models.Model):
    """Class for making different feedbacks"""
    text = models.CharField(verbose_name='Feedback', max_length=500)
    grade = models.IntegerField(verbose_name='Grade')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    subject = models.CharField(verbose_name='Theme', max_length=200)
