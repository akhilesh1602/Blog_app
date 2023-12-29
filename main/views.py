from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from . models import Article

# Create your views here.

def home(request):
    articles = Article.objects.order_by("-created_date")[0:5]
    data = {
        "articles":articles,
    }
    return render(request, "home.html",data)

def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        Article.objects.create(title=title, description=description)
        
    return render(request, "create_post.html")

def login(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("login successfully !")

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
            return HttpResponse("register successfully")
        else:
            return HttpResponse("password and confirm password not equal !")
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

