from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import SignUpForm, LoginForm, TeamForm
from django.contrib.auth.models import User
from .models import Account, Team


def home(request):
    team = None
    if Account.objects.filter(username=request.user.username).exists():
        account_user = Account.objects.get(username=request.user.username)
        if account_user.team is not None:
            team = account_user.team.name
            return render(request, 'home.html', context={'team': team})

    return render(request, 'home.html', context={'team': team})


def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get('email')
            account_user = Account.objects.create_user(username=username, email=email, password=password)
            login(request, account_user)
            return redirect("team")

        else:
            return redirect('signup')

    return render(request, "signup.html", context={"form": form})


def login_account(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    return redirect("login")
            else:
                return redirect("login")
        else:
            return redirect("login")
    return render(request, 'login.html', context={'form': form})


def logout_account(request):
    logout(request)
    return redirect("login")


@login_required
def joinoradd_team(request):
    user = request.user
    form = TeamForm()

    # Handle POST request to create or join a team
    if request.method == "POST":
        user = request.user
        form = TeamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')  # Use 'name' instead of 'team'

            # Check if a team with the given name already exists
            if Team.objects.filter(name=name).exists():
                team = Team.objects.get(name=name)
            else:
                # Create a new team if it doesn't exist
                team = Team.objects.create(name=name, jitsi_url_path=f'http://meet.jit.si/{name}')

            # Associate the user with the team
            if Account.objects.filter(username=user.username).exists():
                account_user = Account.objects.get(username=user.username)
                account_user.team = team
                account_user.save()
                return redirect("home")
            return redirect("home")

        else:
            print(form.errors)  # Add this for debugging invalid form errors
            return redirect("home")  # If the form is not valid, redirect to home for now
    if Account.objects.filter(username=user.username).exists():
        account_user = Account.objects.get(username=user.username)
        if account_user.team is not None:
            return redirect("home")

    return render(request, 'team.html', context={"form": form})


def exit_team(request):
    if Account.objects.filter(username=request.user.username):
        account_user = Account.objects.get(username=request.user.username)
        account_user.team = None
        account_user.save()
    return redirect("home")
