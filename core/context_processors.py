from .models import AnimalProfile, Bond, Message

def notification_counts(request):
    if not request.user.is_authenticated:
        return {}
    
    try:
        profile = AnimalProfile.objects.get(user=request.user)
        pending_notifications_count = Bond.objects.filter(to_animal=profile, status='Pending').count()
        unread_messages_count = Message.objects.filter(receiver=profile, is_read=False).count()
        
        return {
            'pending_notifications_count': pending_notifications_count,
            'unread_messages_count': unread_messages_count
        }
    except AnimalProfile.DoesNotExist:
        return {}
