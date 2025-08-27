from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm


# list all the posts by users
class PostListView(View):
    def get(self, request, *args, **kwargs):
        # collect all post and sort them newest to oldest
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'group_chat/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'group_chat/post_list.html', context)
