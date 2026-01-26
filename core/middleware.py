from django.utils import timezone
from .models import AnimalProfile

class PresenceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                # Update last activity for the user's profile
                AnimalProfile.objects.filter(user=request.user).update(last_activity=timezone.now())
            except:
                pass
        
        response = self.get_response(request)
        return response
