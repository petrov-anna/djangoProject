from django.views.generic import ListView, TemplateView
from .models import Post


class BlogListView(ListView):
    paginate_by = 2
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ImputationPageView(TemplateView):
    template_name = 'imputation.html'
