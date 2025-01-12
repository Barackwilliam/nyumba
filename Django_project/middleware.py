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
            

     