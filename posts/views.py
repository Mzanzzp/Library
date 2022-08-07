from django.shortcuts import render

# Create your views here.
from comments.forms import CommentForm
from comments.models import CommentPost
from posts.forms import PostForm
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
    post = Post.objects.get(pk=post_id)


    if request.method == "POST":
        print(request.POST)
        post_form = PostForm(request.POST)
        # comment_form = CommentForm(request.POST)
        if 'post_submit' in request.POST:
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                print("1")
                post.title = post_form.cleaned_data['title']
                post.content = post_form.cleaned_data['content']
                post.save()
        elif "comment_submit" in request.POST:
            comment_form = CommentForm(request.POST)
            print("cos")
            if comment_form.is_valid():
                print('2')
                data = dict(comment_form.cleaned_data)
                data['post'] = post
                comment = CommentPost.objects.create(**data)

    data = {'title': post.title, 'content': post.content}
    post_form = PostForm(data=data)
    comment_form = CommentForm()


    return render(
        request,
        "posts/details.html",
        context={"post": post, "comment_form": comment_form, "post_form": post_form},
    )



