from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Post, Comment


def blog(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method =='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form':form })


@login_required
def delete_comment(request, comment_id):
    """ Delete comment from blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('blog'))
