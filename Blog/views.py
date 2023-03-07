from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect

from.models import *

from django.contrib.auth.models import User

# Create your views here.
def index(request):
        obj = {'blogs':Blogpost.objects.all()}
        return render(request, 'home.html', obj)
        






def blogfun(request):
    if request.method == 'POST':
                title=request.POST['tt']
                content=request.POST['mt']  
                image=request.POST['st']
                s1=Blogpost()
                s1.title=title
                s1.content=content
                s1.image=image
                s1.save()
                return redirect('index')
                                        



    return render(request,'add.html')


def post(request,id):

    try:
        post = Blogpost.objects.get(id=id)
        # print(post)
    except Blogpost.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'display.html', {'post': post})



def signup(request):
    if request.method=="POST":
        uname=request.POST['upuname']
        upass=request.POST['uppsw']
        umail=request.POST['upemail']

        if User.objects.filter(Q(username=uname)|  Q(email=umail)).exists():
            return render(request,'signup.html',{'error':"user already exit"})
        else:
            user=User.objects.create_user(username=uname,password=upass,email=umail)
            user.save()
            return  redirect('login')





    return render(request,'signup.html')





@login_required(login_url='index')
def loginfun(request):
    if request.method=="POST":
                uname=request.POST['marta']
                passw=request.POST['karta']
                user=authenticate(username=uname,password=passw)

                if user is not None:
                    login(request,user)
                    return redirect('index')

                else:
                    return render(request,'sign.html',{"errorsign":"invalid credintials"})
                    # return redirect('login_up')

    return render(request,'sign.html')

def search(request):
    if request.method == 'POST':
        quote=request.POST['quote']
        results = Blogpost.objects.get(title=quote)
        print(results)


        return render(request, 'search.html', {'quotes': results})


    else:
        notfound = "BLOG POST NOT FOUND"
        return render(request, 'search.html', {'notfound': notfound})

