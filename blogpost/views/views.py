from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.template import RequestContext
from django.shortcuts import render
from django import forms
from django.db.models import Q
from blogpost.models.models import *
from markdownx.utils import markdownify



# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def archive(request):
    template_name = 'blogs.html' 
    blogs = Post.objects.order_by('date')
    return render(request, template_name, {'blogs': blogs})


def search_keywords(request):
    form_data = request.GET
    iterable_form_data = form_data.dict()
    search_box = iterable_form_data['Search']
    template_name = 'blogs.html'
    posts_head = Post.objects.filter(content__text__contains=search_box)
    if posts_head.exists():
        print(posts_head)
        return render(request, template_name, {'blogs': posts_head, 'search_box': search_box})
    else: 
        template_name = '404.html'
        return render(request, template_name)

def popular(request):
    blogs = Post.objects.order_by('post_like')
    template_name = 'blogs.html'
    return render(request, template_name, {'blogs': blogs})    

def filter_blog_by_topic(request, topic_type):
    topic = topic_type
    blogs = Post.objects.filter(tags = topic)
    template_name = 'blogs.html'
    return render(request, template_name, {'blogs': blogs, 'topic': topic})

def blog(request):
    blogs = Post.objects.order_by('date')[:5]
    template_name = 'blogs.html'
    return render(request, template_name, {'blogs': blogs})    


def projects(request):
    template_name = 'projects.html'
    return render(request, template_name)    

def get_this_post(request, blog_id):
    template_name = 'post.html'
    post = Post.objects.get(pk= blog_id)
    print("im the content", post.content)
    print("this is what I am", type(post.content))
    # for post in post:
    # post.text = markdownify(post.content.text)
    print("this is post.text", type(post.content.text))
    return render(request, template_name, {'post': post})


