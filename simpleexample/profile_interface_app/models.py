from django.db import models

# Create your models here.
class LinkedInSettings(models.Model):
    user_token = models.CharField(max_length=100)
    user_secret = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)


class SocialSetup(models.Model):
    social_name = models.CharField(max_length=48)
    social_url = models.URLField()
    social_enabled = models.BooleanField()
    social_icon = models.CharField(max_length=32)


class SectionsSetup(models.Model):
    section_name = models.CharField(max_length=128)
    section_order = models.PositiveIntegerField()
    section_enabled = models.BooleanField()
    section_component_template = models.CharField(max_length=200)
