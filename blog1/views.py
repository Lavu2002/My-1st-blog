from django.shortcuts import render 
from django.template.loader import render_to_string
from blog1.models import Post
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def blog1Home(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog1/blog1Home.html',context)


def blog1Post(request,pk):
    print("check1")
    post= get_object_or_404(Post,pk=pk)
    return render(request,'blog1/blog1Post.html',context={'post':post})

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    print("print2")
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {'post': post,'is_liked': is_liked,'totallikes': post.total_likes()}
    if request.is_ajax():
        print("print1")
        html = render_to_string('blog1/like_section.html', context, request=request)
        return JsonResponse({'form': html})