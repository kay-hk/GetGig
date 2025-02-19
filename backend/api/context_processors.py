from django.conf import settings

def logged_in_status(request):
    return {
        'loggedIn': request.session.get('loggedIn', False)  # or use any session variable
    }