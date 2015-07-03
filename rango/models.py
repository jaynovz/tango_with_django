from django.db import models
from django.contrib.auth.models import User
from managers import JssorMediaManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = "Categories"


    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class JssorMedia(models.Model):
    file = models.FileField(upload_to='jssor_media/')
    alternate_file_name = models.CharField(max_length=200, null=True)
    alt_text = models.CharField(max_length=200, null=True)
    uploaded = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        if self.alternate_file_name:
            return self.alternate_file_name
        return file.name
