from django.shortcuts import render
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# list all the posts and create new post
class PostListView(LoginRequiredMixin, View):
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

# get details of a post
class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'group_chat/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'group_chat/post_detail.html', context)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body']
    #form_class = PostForm
    template_name = 'group_chat/post_edit.html'

# redirect back to post detail view
    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse_lazy('chat:post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'group_chat/post_delete.html'
    success_url = reverse_lazy('chat:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'group_chat/comment_edit.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

def get_success_url(self):
    return reverse_lazy('chat:post-detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'group_chat/comment_delete.html'
    

    def get_success_url(self):
        return reverse_lazy('chat:post-detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
         comment = self.get_object()
         return self.request.user == comment.author
