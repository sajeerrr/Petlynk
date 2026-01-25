from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, AnimalProfileForm
from .models import AnimalProfile
from .matching import get_matches
from .models import Bond
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(
                request,
                "reg.html",
                {"error": "Invalid username or password", "mode": "login", "form": RegisterForm()}
            )

    return render(request, "reg.html", {"mode": "login", "form": RegisterForm()})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('create_profile')
        else:
             # Stay in register mode on error
            return render(request, 'reg.html', {'form': form, 'mode': 'register'})
    else:
        form = RegisterForm()

    return render(request, 'reg.html', {'form': form, 'mode': 'register'})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = AnimalProfileForm(request.POST, request.FILES)
        if form.is_valid():

            if AnimalProfile.objects.filter(user=request.user).exists():
                return redirect('dashboard')

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('dashboard')
    else:
        form = AnimalProfileForm()

    return render(request, 'create_profile.html', {'form': form})


@login_required
def edit_profile(request):
    try:
        profile = AnimalProfile.objects.get(user=request.user)
    except AnimalProfile.DoesNotExist:
        return redirect('create_profile')

    if request.method == 'POST':
        form = AnimalProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AnimalProfileForm(instance=profile)

    return render(request, 'create_profile.html', {'form': form, 'is_edit': True})



@login_required
@login_required
def dashboard(request):
    try:
        profile = AnimalProfile.objects.get(user=request.user)
    except AnimalProfile.DoesNotExist:
        return redirect('create_profile')

    matches = get_matches(profile)

    if request.method == "POST":
        target_id = request.POST.get("target")
        target = AnimalProfile.objects.get(id=target_id)

        Bond.objects.get_or_create(
            from_animal=profile,
            to_animal=target,
            defaults={"score": 10}
        )

    # Mutual matches
    mutuals = Bond.objects.filter(
        from_animal=profile,
        to_animal__in=Bond.objects.filter(
            to_animal=profile
        ).values("from_animal")
    )

    return render(request, "dashboard.html", {
        "profile": profile,
        "matches": matches,
        "mutuals": mutuals
    })


def forgot_password(request):
    from .forms import ForgotPasswordForm
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email__iexact=email)
            # Redirect to the reset page with the username as a simple identifier
            # (In production, use a secure token)
            return redirect('reset_password', username=user.username)
    else:
        form = ForgotPasswordForm()
    
    return render(request, "reset.html", {"form": form, "step": 1})


def reset_password(request, username):
    from .forms import SetNewPasswordForm
    user = User.objects.get(username=username)
    
    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            return redirect('user_login')
    else:
        form = SetNewPasswordForm()
    
    return render(request, "reset.html", {"form": form, "step": 2, "reset_user": user})



