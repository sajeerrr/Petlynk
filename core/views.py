from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
                "auth.html",
                {"error": "Invalid username or password", "mode": "login", "form": RegisterForm()}
            )

    return render(request, "auth.html", {"mode": "login", "form": RegisterForm()})


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
            return render(request, 'auth.html', {'form': form, 'mode': 'register'})
    else:
        form = RegisterForm()

    return render(request, 'auth.html', {'form': form, 'mode': 'register'})


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
def dashboard(request):
    profile = AnimalProfile.objects.get(user=request.user)
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


