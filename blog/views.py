from django.views.generic import ListView, TemplateView
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from .models import Post


class BlogListView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RecognitionPageView(TemplateView):
    template_name = 'recognition.html'


class PredictionPageView(TemplateView):
    template_name = 'prediction.html'


class ClassificationPageView(TemplateView):
    template_name = 'classification.html'


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("blog:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("blog:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "You were log out success!")
    return redirect("blog:home")
