from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render



def my_passwordchange(request):
    password_form = PasswordChangeForm(data=request.POST or None,
                                       user=request.user)
    print "VALIT!!0"
    if request.method == "POST":
        print "VALIT!!1"
        if password_form.is_valid():
            print "VALIT!!"
            password_form.save()
            return HttpResponseRedirect(reverse('backend_main'))

    to_return = {}
    to_return['change_pass_form'] = password_form

    return render(request, 'auth/change_password.html', to_return)



def my_login(request):
    login_form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST":
        if login_form.is_valid():
            user = authenticate(
                        username=login_form.cleaned_data.get('username'),
                        password=login_form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('backend_main'))
            else:
                return HttpResponseRedirect(reverse('login'))

    to_return = {}
    to_return['login_form'] = login_form

    return render(request, 'auth/login.html', to_return)


def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
