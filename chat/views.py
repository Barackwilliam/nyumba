from django.shortcuts import render, redirect

def chat_page(request):
    # if not request.user.is_authenticated:
    #     return redirect("login")  *args, **kwargs
    # context = {}
    return render(request, "core/chat.html")
    
    
    # (request, "core/chatpage.html", context)
