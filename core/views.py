from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, AnimalProfileForm
from .models import AnimalProfile, Bond, Message
from .matching import get_matches
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
        "mutuals": mutuals,
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


@login_required
def send_bond_request(request):
    if request.method == "POST":
        import json
        from django.http import JsonResponse
        data = json.loads(request.body)
        target_id = data.get("target_id")
        
        try:
            from_profile = AnimalProfile.objects.get(user=request.user)
            to_profile = AnimalProfile.objects.get(id=target_id)
            
            # Check if bond already exists
            bond, created = Bond.objects.get_or_create(
                from_animal=from_profile,
                to_animal=to_profile,
                defaults={"status": "Pending", "score": 10}
            )
            
            return JsonResponse({"status": "success", "created": created})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return redirect('dashboard')


@login_required
def notifications_view(request):
    try:
        profile = AnimalProfile.objects.get(user=request.user)
    except AnimalProfile.DoesNotExist:
        return redirect('create_profile')

    # Get pending bonds received by this animal
    pending_bonds = Bond.objects.filter(to_animal=profile, status='Pending').order_by('-created_at')
    
    # Mark as notified (optional for later badge logic)
    pending_bonds.update(notified=True)

    return render(request, "notifications.html", {
        "profile": profile,
        "pending_bonds": pending_bonds
    })


@login_required
def accept_bond(request, bond_id):
    try:
        profile = AnimalProfile.objects.get(user=request.user)
        bond = Bond.objects.get(id=bond_id, to_animal=profile)
        bond.status = 'Accepted'
        bond.save()
        
        # Create a reciprocal bond if it doesn't exist for chat logic
        Bond.objects.get_or_create(
            from_animal=bond.to_animal,
            to_animal=bond.from_animal,
            defaults={"status": "Accepted", "score": 10}
        )
        
    except Bond.DoesNotExist:
        pass
        
    return redirect('notifications')


@login_required
def chat_list(request):
    try:
        profile = AnimalProfile.objects.get(user=request.user)
    except AnimalProfile.DoesNotExist:
        return redirect('create_profile')

    # Get all accepted bonds (reciprocal or sent)
    accepted_bonds = Bond.objects.filter(
        from_animal=profile,
        status='Accepted'
    ).select_related('to_animal')

    return render(request, "chat_list.html", {
        "profile": profile,
        "accepted_bonds": accepted_bonds
    })


@login_required
def chat_room(request, profile_id):
    try:
        my_profile = AnimalProfile.objects.get(user=request.user)
        other_profile = AnimalProfile.objects.get(id=profile_id)
        
        # Verify bond exists and is accepted
        if not Bond.objects.filter(from_animal=my_profile, to_animal=other_profile, status='Accepted').exists():
            return redirect('dashboard')
            
        from django.db.models import Q
        messages = Message.objects.filter(
            (Q(sender=my_profile) & Q(receiver=other_profile)) |
            (Q(sender=other_profile) & Q(receiver=my_profile))
        ).order_by('timestamp')
        
        # Mark received messages as read
        messages.filter(receiver=my_profile, is_read=False).update(is_read=True)

        return render(request, "chat_room.html", {
            "my_profile": my_profile,
            "other_profile": other_profile,
            "messages": messages
        })
    except (AnimalProfile.DoesNotExist):
        return redirect('dashboard')


@login_required
def send_message(request, profile_id):
    if request.method == "POST":
        import json
        from django.http import JsonResponse
        data = json.loads(request.body)
        content = data.get("content")
        
        if not content:
            return JsonResponse({"status": "error", "message": "Content is empty"})

        try:
            my_profile = AnimalProfile.objects.get(user=request.user)
            other_profile = AnimalProfile.objects.get(id=profile_id)
            
            # Verify bond
            if not Bond.objects.filter(from_animal=my_profile, to_animal=other_profile, status='Accepted').exists():
                return JsonResponse({"status": "error", "message": "Bond not accepted"})

            msg = Message.objects.create(
                sender=my_profile,
                receiver=other_profile,
                content=content
            )
            
            return JsonResponse({
                "status": "success", 
                "msg_id": msg.id,
                "content": msg.content,
                "timestamp": msg.timestamp.strftime("%I:%M %p")
            })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Method not allowed"})



