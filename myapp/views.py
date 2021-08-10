from django import forms
from django.contrib.messages.api import warning
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from myapp.models import Blog
from myapp.forms import Edit_blog
# Create your views here.

def index(request):

    blog = Blog.objects.all()
    context = {'blogs':blog}
       # return HttpResponse("<h1>hello this is index page</h1>")
    return render(request,'index.html',context)

def about(request): 
    #return HttpResponse("<h1>hello this is about page</h1>")
    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('passwords')

        if pass1!=pass2:
            messages.warning(request,"Password Does Not Match")
            return redirect('register')

        elif User.objects.filter(username=uname).exists():
            messages.warning(request,"Username already taken")
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Email already taken")
            return redirect('register')


        #print(fname,lname,uname,email,pass1,pass2)
        else:

            users = User.objects.create_user(first_name=fname,last_name=lname,username=uname,
            email=email,password=pass1)
            users.save()
            messages.success(request, 'User Has Been Register Successfully')
            return redirect('login')
    #return HttpResponse("<h1>hello this is register page</h1>")
    return render(request,'register.html')

def user_login(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
          login(request, user)
          return redirect('/')

        else:
           messages.warning(request,"Invalid Credentials")
           return redirect('login')

    #return HttpResponse("<h1>hello this is login page</h1>")
    return render(request,'login.html') 

def user_logout(request):
    logout(request)
    return redirect('/')

def user_blog(request):

    if request.method=="POST":
        title = request.POST.get('titles')
        desc = request.POST.get('descs')
        
        blog = Blog(title=title,desc=desc,user_id=request.user)
        blog.save()

        messages.success(request,"Your Post has been submitted suceessfully")

        return redirect('post_blog')
       # print(title,desc)
    return render(request,'blog.html')

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    
    return render(request,'blog_detail.html',context)

def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,"Blog has been deleted")
    return redirect("/")

def edit(request,id):
    blog = Blog.objects.get(id=id)

    edit = Edit_blog(instance= blog)

    if request.method=="POST":
        form = Edit_blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,"Post has been updated")

            return redirect("/")


    return render(request,'edit_blog.html',{'edit_blog':edit})
