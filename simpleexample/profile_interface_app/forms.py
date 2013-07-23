from django.forms import ModelForm
from profile_interface_app.models import LinkedInSettings

class LinkedInSetupForm(ModelForm):
    class Meta:
        model = LinkedInSettings



