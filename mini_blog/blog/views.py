from django.shortcuts import render, redirect
from blog.models import Blog_user, Comments, Like
from django.views.generic.base import View
from .forms import FormComment
from django.shortcuts import get_object_or_404

class PostView(View):
    def get(self, request):
        getting_data = Blog_user.objects.all()
        
        return render(request, 'blog/home.html',{'getting_data' : getting_data})


class PostDetail(View):
    def get(self, request, pk):
        detail = Blog_user.objects.get(id=pk)
        comments = Comments.objects.filter(to_which_post=detail)
        return render(request, 'blog/detail_post.html', {'getting_data' : detail, 'comments': comments})
    
    
class AddComments(View):
    def post(self, request, pk):
        form = FormComment(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            post = get_object_or_404(Blog_user, pk=pk)
            comment.to_which_post = post 
            comment.save() 
            
        ret = request.META.get('HTTP_REFERER')
        return redirect(ret)
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    return ip


class AddLike(View):
    def get(self, request, pk):
        client_ip = get_client_ip(request)
        ret = request.META.get('HTTP_REFERER')
        
        try:
            Like.objects.get(ip=client_ip, pos_id = pk)
            return redirect(ret)
        except:
            new_like = Like()
            new_like.ip = client_ip
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(ret)
        
class AddDisLike(View):
    def get(self, request, pk):
        client_ip = get_client_ip(request)
        ret = request.META.get('HTTP_REFERER')
        
        try:
            like_delete = Like.objects.get(ip=client_ip)
            like_delete.delete()
            return redirect(ret)
        except:
            return redirect(ret)