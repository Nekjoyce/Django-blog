from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
