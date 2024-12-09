from django.shortcuts import redirect
from django.urls import reverse




class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        active_urls = [reverse('index'), reverse('reg')]
        if not request.user.is_authenticated and request.path not in active_urls:
            return redirect(reverse('index'))
        response = self.get_response(request)
        return response