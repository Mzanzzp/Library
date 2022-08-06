from django.shortcuts import render

# Create your views here.
from posts.models import Post


def listview(request):
    posts = Post.objects.all()
    print(request.method)
    print(request.user)
    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
        )
    return render(
        request,
        "posts/list.html",
        {"posts": posts}
    )

def details(request, post_id):
    post = Post.object.get(pk=post_id)

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        post.title = title
        post.content = content

        post.save()

    return render(
        request,
        "post/details.html",
        {"post": post},
    )

