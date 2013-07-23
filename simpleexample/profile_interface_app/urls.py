from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^backend/linkedin',
        'profile_interface_app.views.backend_set_linkedin_information',
        name='backend_linkedin'),
    url(r'^backend/sections_setup',
        'profile_interface_app.views.backend_configure_sections',
        name='backend_sections'),
    url(r'^backend/social_section',
        'profile_interface_app.views.backend_social_buttons',
        name='backend_social_buttons'),
    url(r'^backend/', 'profile_interface_app.views.backend_main',
        name='backend_main'),
    url(r'^$', 'profile_interface_app.views.main', name='home'),
    # url(r'^simpleexample/', include('simpleexample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
