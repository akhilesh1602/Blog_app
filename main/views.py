from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from . models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    articles = Article.objects.order_by("-created_date")
    data = {
        "articles":articles,
    }
    return render(request, "home.html",data)

@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        Article.objects.create(title=title, description=description, author = request.user)
        
    return render(request, "create_post.html")

def login(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            return redirect('dashboard')

        else:
            return HttpResponse("invalid username or password")

            
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["user_name"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                return HttpResponse("username already exists !")
            
            elif User.objects.filter(email = email):
                return HttpResponse("email already registered !")
            
        
            user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, email=email, username=username, password=password)
            user.save()
            messages.success(request, 'Registered Successfully !')
            return redirect('login')
        else:
            return HttpResponse("password and confirm password not equal !")
    return render(request, 'register.html')

@login_required(login_url="/login")
def logout(request):
    auth.logout(request)
    messages.success(request, 'logged out!')
    return redirect("login")

@login_required(login_url="/login")
def dashboard(request):
    instances = Article.objects.all().filter(author = request.user)
    name = request.user.first_name
    data = {
        "instances": instances,
        "name":name,
    }
    return render(request, "dashboard.html", data)

def get_articles(request, pk):
    instances = Article.objects.all().order_by("created_date").filter(author_id = pk)
    for i in instances:
        name = i.author
        break
    data = {
        "articles" : instances ,
         "name" : name
    }
    return render(request, "get_articles.html", data)

@login_required(login_url="/login")
def comments(request, pk):
    if request.method == "POST":
        instance = request.POST['comment']
        Comment.objects.create(description = instance, comment_by = request.user)
        
        return render(request, "comments.html")

    else:
        instances = Comment.objects.all().order_by("created_date").filter(article_description = pk)
        data = {
           "instances" : instances,
        }
        return render(request, "comments.html", data)
    


