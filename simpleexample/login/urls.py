from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/', 'login.views.my_login', name='login'),
    url(r'^logout/', 'login.views.my_logout', name='logout'),
    url(r'^changepassword/', 'login.views.my_passwordchange', name='backend_pass_change'),
    # url(r'^simpleexample/', include('simpleexample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
