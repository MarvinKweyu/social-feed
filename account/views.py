from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(
                request, username=clean_data['username'], password=clean_data['password'])  # check credentials

            if user is not None:
                if user.is_active:
                    login(request, user)  # set current session
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        #  when called with a GET, just render
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
