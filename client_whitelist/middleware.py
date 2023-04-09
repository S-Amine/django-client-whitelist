from django.http import HttpResponseForbidden
from django.conf import settings
from datetime import datetime

class ClientWhitelistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current time and format it as string
        now = datetime.now()
        formatted_date = now.strftime("[%d/%b/%Y %H:%M:%S]")

        # Get client host IP address or domain name
        referer = request.META.get('HTTP_REFERER', '')
        if referer:
            client_host = referer.split('/')[2]
        else:
            client_host = request.META.get('REMOTE_ADDR')

        # Get protected endpoints and allowed client hosts from settings
        PROTECTED_ENDPOINTS = settings.PROTECTED_ENDPOINTS
        ALLOWED_CLIENT_HOSTS = settings.ALLOWED_CLIENT_HOSTS

        # Check if request is for a protected endpoint
        if any(request.path.startswith(endpoint) for endpoint in PROTECTED_ENDPOINTS):
            # Check if all client hosts are allowed
            if '*' in ALLOWED_CLIENT_HOSTS:
                print('\033[92m' + formatted_date, "Allowed request from:", client_host + '\033[0m')
                return self.get_response(request)
            # Check if client host is in the allowed list
            elif client_host not in ALLOWED_CLIENT_HOSTS:
                print('\033[91m' + formatted_date, "Banned request from:", client_host + '\033[0m')
                return HttpResponseForbidden()

        # If request is not for a protected endpoint or client is allowed, continue with request
        print('\033[92m' + formatted_date, "Allowed request from:", client_host + '\033[0m')
        return self.get_response(request)

