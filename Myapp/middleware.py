# myapp/middleware.py
from django.utils import translation
from django.conf import settings

class PersistentLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Check cookie
        lang = request.COOKIES.get('django_language')
        
        # 2. Fallback to browser language
        if not lang:
            lang = request.META.get('HTTP_ACCEPT_LANGUAGE', settings.LANGUAGE_CODE)[:2]
            if lang not in dict(settings.LANGUAGES):
                lang = settings.LANGUAGE_CODE
        
        # 3. Activate language
        translation.activate(lang)
        request.LANGUAGE_CODE = lang
        
        response = self.get_response(request)
        
        # 4. Set cookie if not present
        if not request.COOKIES.get('django_language'):
            response.set_cookie('django_language', lang, max_age=315360000)  # 10 years
        
        return response



