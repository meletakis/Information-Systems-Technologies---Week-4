from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from posts.models import Posts,Comments
from posts.forms import PostsForm, CommentsForm
# Create your views here.
import json
import urllib2

@login_required
def index(request):
     data = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts'))
     context = {'data' : data}
     return render(request, 'allposts.html', context)

@login_required
def getpost(request, postid):
     post = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+postid))
     comments = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+postid+'/comments' ))
     context = {'post' : post, 'comments':comments}
     return render(request, 'post.html', context)

@login_required
def getuser(request, userid):
     user = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/users/'+userid))
     user_posts= json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts?userId='+userid))
     context = {'user' : user,'user_posts' : user_posts }
     return render(request, 'user.html', context)

@login_required
def getposts_from_model(request):
     data = Posts.objects.all()
     context = {'data' : data}
     return render(request, 'allposts.html', context)

@login_required
def getposts_from_model_by_id(request,postid):
     post = Posts.objects.get(pk=postid)
     comments = Comments.objects.filter(postId=postid)
     form = CommentsForm()
     context = {'post' : post, 'comments':comments, 'form':form,}
     return render(request, 'post.html', context)

@login_required
def http_resp(request):
    return HttpResponse("Rango says hey there world!")


def post_form(request):
     if request.method == 'GET':
          form = PostsForm()
     else:
          form = PostsForm(request.POST)
          if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Posts.objects.create(title=title,body=body,userId = request.user)
            return HttpResponseRedirect("/posts/"+str(post.id))


     return render(request, 'newpost.html', {
        'form': form,
    })

def comments_form(request,postid):
     if request.method == 'POST':
          form = CommentsForm(request.POST)
          if form.is_valid():
            name = form.cleaned_data['name']
            body = form.cleaned_data['body']
            email = form.cleaned_data['email']
            post = Posts.objects.get(id=postid)
            comment = Comments.objects.create(name=name,body=body,postId=post, email=email)
            return HttpResponseRedirect("/posts/"+str(postid))
     else:      
          return HttpResponseRedirect("/posts/"+str(postid))