from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from account.forms import (LoginForm, ProfileForm, UserEditForm,
                           UserRegistrationForm)
from account.models import Contact, Profile
from actions.models import Action
from actions.utils import create_action
from common.decorators import ajax_required

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


@login_required
def dashboard(request):
    """Landing page dashboard"""
    # get all actions for display other than the current user's
    actions = Action.objects.exclude(user=request.user)
    # get users this user is following
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related(
        'user', 'user__profile').prefetch_related('target')[:10]
    # section is used to identify where the user is currently browsing
    return render(request, "account/dashboard.html", {'section': 'dashboard', 'actions': actions})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create new user
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, "created an account")
            return render(request, "account/register_done.html", {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/register.html", {'user_form': user_form})


@login_required
def edit_user(request):
    """Edit an existing user details"""
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")

    return render(request, "account/edit.html", {"user_form": user_form, "profile_form": profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    """Follow a specific user"""
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user, user_to=user)
                create_action(request.user, "followed", user)
            else:
                # unfollow
                Contact.objects.filter(
                    user_from=request.user, user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})
