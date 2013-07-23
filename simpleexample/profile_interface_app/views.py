import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from linkedin import linkedin

from common.secure_vars import *
from profile_interface_app.models import LinkedInSettings
from profile_interface_app.forms import LinkedInSetupForm

from profile_interface_app.models import SocialSetup
from profile_interface_app.models import SectionsSetup

LOG = logging.getLogger(__name__)


#@cache_page(60 * 60) # This will reduce the number of requests to LinkedIn
def main(request):
    LOG.debug('Request on Main')
    linkedin_settings = None
    try:
        linkedin_settings = LinkedInSettings.objects.get(id=1)
    except LinkedInSettings.DoesNotExist:
        return HttpResponseRedirect(reverse('backend_main'))

    authentication = linkedin.LinkedInDeveloperAuthentication(
                                    linkedin_settings.api_key,
                                    linkedin_settings.api_secret,
                                    linkedin_settings.user_token,
                                    linkedin_settings.user_secret,
                                    "",
                                    linkedin.PERMISSIONS.enums.values())

    application = linkedin.LinkedInApplication(authentication)
    profile = None
    try:
        profile = application.get_profile(selectors=[
                                    'summary',
                                    'skills',
                                    'educations',
                                    'positions',
                                    'picture-url',
                                    'phone-numbers',
                                    'main-address',
                                    'languages:(language,proficiency)',
                                    'email-address',
                                    'first-name',
                                    'last-name'])

    except linkedin.LinkedInError, e:
        LOG.debug('Error detected: {0}'.format(str(e)))

    if profile:
        try:
            all_sections = SectionsSetup.objects.all().order_by('section_order')
        except SectionsSetup.DoesNotExist:  # No settings yet...
            all_sections = []

        to_return = {}
        to_return['sections_to_show'] = all_sections

        to_return['social_buttons'] = SocialSetup.objects.all()

        #to_return['icons_bordered'] = True
        to_return['full_name'] = " ".join([profile['firstName'], profile['lastName']])
        to_return['summary'] = profile['summary']
        to_return['main_address'] = profile['mainAddress']
        to_return['phone_numbers'] = profile['phoneNumbers']
        to_return['email_address'] = profile['emailAddress']
        to_return['skills'] = profile['skills']['values']
        to_return['languages'] = profile['languages']
        to_return['positions'] = profile['positions']['values']
        to_return['educations'] = profile['educations']['values']
        to_return['personal_picture'] = profile['pictureUrl']

        return render(request, 'cv/main.html', to_return)
    else:
        return HttpResponse("Error connecting LinkedIn.")


def backend_main(request):
    to_return = {}
    return render(request, 'cv/backend_main.html', to_return)


def backend_set_linkedin_information(request):
    if request.method == 'POST':
        form = LinkedInSetupForm(request.POST)
        if form.is_valid():
            configuration = form.save()
            try:
                linkedin_settings = LinkedInSettings.objects.get(id=1)
            except LinkedInSettings.DoesNotExist:
                linkedin_settings = LinedInSettings(configuration)
            finally:
                linkedin_settings.save()

            return HttpResponseRedirect(reverse('backend_main'))
    else:
        try:
            linkedin_settings = LinkedInSettings.objects.get(id=1)
        except LinkedInSettings.DoesNotExist:  # No settings yet...
            form = LinkedInSetupForm()
        else:       # If the settings has been already set
            form = LinkedInSetupForm(instance=linkedin_settings)

    to_return = {}
    to_return['formLinkedInSetup'] = form
    return render(request, 'cv/backend_linkein_account.html', to_return)


def backend_social_buttons(request):
    if request.method == 'POST':
            """TODO: Change to generate dynamic form based on the DB
                     content."""
            for social_button_name in request.POST:
                if social_button_name == 'csrfmiddlewaretoken':
                    continue

                url_to_save = request.POST[social_button_name]

                social_button = SocialSetup.objects.get(
                                         social_name=social_button_name)

                social_button.social_url = url_to_save
                social_button.save()

            return HttpResponseRedirect(reverse('backend_main'))
    else:
        try:
            all_socialbuttons = SocialSetup.objects.all()
            print(all_socialbuttons)
        except SocialSetup.DoesNotExist:
            all_socialbuttons = "Empty"

    to_return = {}
    to_return['socialbuttons'] = all_socialbuttons

    return render(request, 'cv/backend_social_buttons.html', to_return)


def backend_configure_sections(request):
    if request.method == 'POST':
        positions = request.POST.get('sections_order', None)
        if positions:
            list_positions = list(positions.split(','))
            for position in list_positions:
                section = SectionsSetup.objects.get(id=position)
                order = list_positions.index(position)
                section.section_order = list_positions.index(position)
                section.save()
    try:
        all_sections = SectionsSetup.objects.all().order_by('section_order')
    except SectionsSetup.DoesNotExist:  # No settings yet...
        all_sections = []

    to_return = {}
    to_return['sections_setup'] = all_sections
    return render(request, 'cv/backend_configure_sections.html', to_return)


