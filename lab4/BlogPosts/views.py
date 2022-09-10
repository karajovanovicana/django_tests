from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from BlogPosts.forms import PostForm, CustomUserForm
from BlogPosts.models import Post, CustomUser


def posts(request):
    queryset = Post.objects.exclude(user__user=request.user).\
        exclude(user__user__in=CustomUser.objects.get(user=request.user).blocked_user.get_queryset())
    context = {"posts": queryset}
    return render(request, "posts.html", context=context)


def profile(request):
    queryset = Post.objects.filter(user__user=request.user).all()
    queryset1 = CustomUser.objects.filter(user=request.user).all()

    context = {"posts": queryset}
    context1 = {"currentuser": queryset1}
    if queryset.count() > 0:
        return render(request, "profile.html", context=context)
    else:
        return render(request, "profile.html", context=context1)


def add_post(request):
    if request.method == "POST":
        form_data = PostForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.user = CustomUser.objects.get(user=request.user)
            post.file = form_data.cleaned_data['file']
            post.save()
            return redirect("profile")

    queryset = Post.objects.filter(user__user=request.user).all()
    context = {"posts": queryset, "form": PostForm}
    return render(request, "post_form.html", context=context)


def blocked_users(request):
    if request.method == "POST":
        instance = CustomUser.objects.get(user=request.user)
        form_data = CustomUserForm(data=request.POST, instance=instance)
        if form_data.is_valid():
            form_data.save()
        return redirect("blocked_users")

    queryset = CustomUser.objects.filter(user=request.user).all()
    context = {"instance": queryset, "form": CustomUserForm}
    return render(request, "blocked_users.html", context=context)
