from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User
from applications.music.models_utils import TimeStampedModel
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime, timedelta

def upload_to(instance, filename):
    return "%s/%s" % (instance._meta.app_label, filename)

class Article(TimeStampedModel, models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False, null=False )
    description = models.TextField(max_length=500, blank=False, null=False )
    image = models.ImageField(
                    upload_to=upload_to,
                    null=False, blank=False
                     )

    def __str__(self):
    	return str(self.title)

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "Article"


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.id})