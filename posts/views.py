from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.http import HttpResponseForbidden

from .models import (
    Post,
    Comment,
    Like,
    AuthorProfile,
    Category,
    Tag
)
def is_author(user):

    try:
        return user.authorprofile.is_author

    except AuthorProfile.DoesNotExist:
        return False



# =========================
# Home
# =========================

def home(request):

    return render(
        request,
        'home.html'
    )



# =========================
# Register
# =========================
def register(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = User.objects.create_user(
            username=username,
            password=password
        )


        login(request, user)


        return redirect('home')


    return render(request,'register.html')
# =========================
# Login
# =========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user:

            login(
                request,
                user
            )


            messages.success(
                request,
                "Login successful!"
            )


            return redirect('home')


        messages.error(
            request,
            "Invalid username or password"
        )


    return render(
        request,
        'login.html'
    )



# =========================
# Logout
# =========================

def logout_view(request):

    logout(request)


    messages.success(
        request,
        "Logout successful!"
    )


    return redirect('login')



# =========================
# Post List
# =========================

from django.core.paginator import Paginator
from django.db.models import Q


def post_list(request):

    posts = Post.objects.filter(
        status='published'
    ).order_by('-created_at')


    # =========================
    # Search
    # =========================

    query = request.GET.get('q')

    if query:

        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )


    # =========================
    # Category Filter
    # =========================

    category = request.GET.get('category')

    if category:

        posts = posts.filter(
            category__name=category
        )



    # =========================
    # Tag Filter
    # =========================

    tag = request.GET.get('tag')

    if tag:

        posts = posts.filter(
            tags__name=tag
        )



    # =========================
    # Pagination
    # =========================

    paginator = Paginator(
        posts,
        5
    )


    page_number = request.GET.get('page')


    posts = paginator.get_page(
        page_number
    )



    # =========================
    # Category & Tag Data
    # =========================

    categories = Category.objects.all()

    tags = Tag.objects.all()



    return render(
        request,
        'post_list.html',
        {
            'posts': posts,
            'query': query,
            'categories': categories,
            'tags': tags
        }
    )
# =========================
# Post Details
# =========================

def post_detail(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    # Draft post only author/admin দেখতে পারবে
    if post.status == 'draft':
        
        if request.user != post.author and not request.user.is_staff:
            return HttpResponseForbidden(
                "You cannot view this draft post"
            )


    # View count increase
    post.view_count += 1
    post.save(
        update_fields=['view_count']
    )


    comments = post.comments.all().order_by(
        'created_at'
    )


    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': comments
        }
    )



# =========================
# Create Post
# =========================

@login_required
def create_post(request):

    if not is_author(request.user):

        return HttpResponseForbidden(
            "Only Authors can create posts"
        )


    if request.method == "POST":

        title = request.POST.get('title')

        content = request.POST.get('content')

        status = request.POST.get('status')

        category_id = request.POST.get('category')

        tag_ids = request.POST.getlist('tags')


        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            status=status,
            category_id=category_id
        )


        post.tags.set(tag_ids)


        messages.success(
            request,
            "Post created successfully!"
        )


        return redirect('post_list')


    return render(
        request,
        'create_post.html',
        {
            'categories': Category.objects.all(),
            'tags': Tag.objects.all()
        }
    )



# =========================
# Edit Post
# =========================

@login_required
def edit_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if post.author != request.user:

        return redirect('post_list')


    if request.method == "POST":

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        post.save()


        messages.success(
            request,
            "Post updated!"
        )


        return redirect(
            'post_detail',
            id=post.id
        )


    return render(
        request,
        'edit_post.html',
        {
            'post': post
        }
    )



# =========================
# Delete Post
# =========================

@login_required
def delete_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if post.author == request.user:

        post.delete()

        messages.success(
            request,
            "Post deleted!"
        )


    return redirect('post_list')
# =========================
# Add Comment
# =========================

@login_required
def add_comment(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if request.method == "POST":

        content = request.POST.get('content')


        Comment.objects.create(
            post=post,
            author=request.user,
            content=content
        )


    return redirect(
        'post_detail',
        id=post.id
    )



# =========================
# Edit Comment
# =========================

@login_required
def edit_comment(request, id):

    comment = get_object_or_404(
        Comment,
        id=id
    )


    if comment.author != request.user:

        return redirect(
            'post_list'
        )


    if request.method == "POST":

        comment.content = request.POST.get('content')

        comment.save()


        return redirect(
            'post_detail',
            id=comment.post.id
        )


    return render(
        request,
        'edit_comment.html',
        {
            'comment': comment
        }
    )



# =========================
# Delete Comment
# =========================

@login_required
def delete_comment(request, id):

    comment = get_object_or_404(
        Comment,
        id=id
    )


    if comment.author == request.user:

        post_id = comment.post.id

        comment.delete()


        return redirect(
            'post_detail',
            id=post_id
        )


    return redirect('post_list')



# =========================
# Like Post
# =========================

@login_required
def like_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    like = Like.objects.filter(
        post=post,
        user=request.user
    )


    if like.exists():

        like.delete()

    else:

        Like.objects.create(
            post=post,
            user=request.user
        )


    return redirect(
        'post_detail',
        id=post.id
    )



# =========================
# Profile
# =========================

@login_required
def profile(request):

    posts = Post.objects.filter(
        author=request.user
    )


    return render(
        request,
        'profile.html',
        {
            'posts': posts
        }
    )
# =========================
# Edit Profile
# =========================

@login_required
def edit_profile(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')


        request.user.username = username
        request.user.email = email


        request.user.save()


        messages.success(
            request,
            "Profile updated successfully!"
        )


        return redirect('profile')


    return render(
        request,
        'edit_profile.html'
    )
# =========================
# Author Dashboard
# =========================

@login_required
def author_dashboard(request):

    if not is_author(request.user):

        return HttpResponseForbidden(
            "Only Authors can access dashboard"
        )


    posts = Post.objects.filter(
        author=request.user
    ).order_by('-created_at')


    return render(
        request,
        'author_dashboard.html',
        {
            'posts': posts
        }
    )
# =========================
# Publish Post
# =========================

@login_required
def publish_post(request, id):

    post = get_object_or_404(
        Post,
        id=id,
        author=request.user
    )

    post.status = 'published'

    post.save()


    messages.success(
        request,
        "Post published successfully!"
    )


    return redirect('author_dashboard')
@login_required
def unpublish_post(request, id):

    post = get_object_or_404(
        Post,
        id=id,
        author=request.user
    )

    post.status = 'draft'

    post.save()


    messages.success(
        request,
        "Post moved to draft!"
    )


    return redirect('author_dashboard')
# =========================
# Public Author Profile
# =========================

def author_profile(request, username):

    author = get_object_or_404(
        User,
        username=username
    )


    posts = Post.objects.filter(
        author=author,
        status='published'
    ).order_by('-created_at')



    return render(
        request,
        'author_profile.html',
        {
            'author': author,
            'posts': posts
        }
    )
    