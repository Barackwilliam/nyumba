#from urllib import response
from django.http import HttpResponseNotAllowed

class MethodNotAllowedMiddleware:
    def __init__(self, get_response):
        self.get_response   = get_response

    def __call__(self, request):
        allowed_methods = ['GET','POST','PUT','DELETE']
        if request.method not in allowed_methods:
            return HttpResponseNotAllowed(allowed_methods)
        response = self.get_response(request)
        return response
    


from django.http import HttpResponseForbidden

class BlockScrapersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_agents = [
            "HTTrack", "WebCopier", "Teleport", "wget", "curl", "Go-http-client"
        ]

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        if any(bot.lower() in user_agent for bot in self.blocked_agents):
            return HttpResponseForbidden("Access Denied")
        return self.get_response(request)

            

     