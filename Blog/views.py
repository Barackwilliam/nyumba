from django.shortcuts import render, redirect, get_object_or_404
from . forms import ContactForm, Comment
from django.core.paginator import Paginator
from .models import  BlogPost
from. forms import CommentForm


# Create your views here.
def Blog_post(request):
    return render(request, 'blog/index.html')

def contact_succes(request):
    return render(request, 'blog/succes.html')


def Contact_us(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_succes')       
    else:
        form = ContactForm()      
        return render(request,'blog/contact.html',{'form':form})
    # except:
    #     return render(request,'blog/contact.html',{'form':form})        



    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']



def post_detail(request,pk):
    post = get_object_or_404(BlogPost, pk=pk)

    #Get all comments related to the post
    comments = post.comments.all().order_by('-created_on')
    #Paginate comment only first 4
    paginator = Paginator(comments,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #Comment from logic
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
    return render(request,'core/blog-details.html',{'post':post, 'comments':page_obj,'form':form, 'page_obj':page_obj})


def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/blog-full-grid.html', {'page_obj':page_obj})


