from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    postagens = Post.objects.all().order_by('-data_criacao')

    return render(request, 'home.html', {'postagens': postagens})
