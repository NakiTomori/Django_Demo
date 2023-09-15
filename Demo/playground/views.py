from django.shortcuts import render,redirect
from django.http import HttpResponse
from playground.models import Blog
from playground.forms import BlogForm

def index(request):
    blogs = Blog.objects.all()
    return render(request,"views.html",{'blogs':blogs})

def addnew(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BlogForm()
    return render(request,'index.html',{'form':form})

def edit(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog': blog})

def update(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST, instance= blog)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'blog': blog})

def keshi(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/')