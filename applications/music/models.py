from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User
from .models_utils import TimeStampedModel
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import datetime, timedelta

def upload_to(instance, filename):
    return "%s/%s" % (instance._meta.app_label, filename)

class Album(models.Model, TimeStampedModel):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False, null=False )
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(default="1995-01-01")
    profile_image = models.ImageField(
                    upload_to=upload_to,
                    null=True, blank=True
                     )

    def __str__(self):
    	return str(self.title)

    class Meta:
        verbose_name_plural = "Albums"
        verbose_name = "Album"


    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'pk':self.id})