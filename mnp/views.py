from django.shortcuts import get_object_or_404, redirect, render
from .models import mnpPost, mnpComment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.


@login_required
def mnphomeView(request):
    return render(request, 'success.html')


@login_required
def mnphome(request):
    context = {
        'posts': mnpPost.objects.all().order_by('-date_posted')
    }
    return render(request, 'mnp/home.html', context)


class mnpPostListView(LoginRequiredMixin, ListView):
    model = mnpPost
    template_name = "mnp/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']


class mnpUserPostListView(ListView):
    model = mnpPost
    template_name = 'mnp/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return mnpPost.objects.filter(author=user).order_by('-date_posted')


class mnpPostDetailView(LoginRequiredMixin, DetailView):
    model = mnpPost
    context_object_name = 'post'
    template_name = 'mnp/post_detail.html'

class mnpPostCreateView(LoginRequiredMixin, CreateView):
    model = mnpPost
    fields = ['title', 'content', 'upload']
    template_name = 'mnp/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class mnpPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = mnpPost
    fields = ['title', 'content', 'upload']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class mnpPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = mnpPost
    success_url = '/MnP/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def add_comment_to_post(request, pk):
    post = get_object_or_404(mnpPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.approve()
            comment.save()
            return redirect('mnppost-detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'mnp/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(mnpComment, pk=pk)
    comment.delete()
    return redirect('mnppost-detail', pk=comment.post.pk)
