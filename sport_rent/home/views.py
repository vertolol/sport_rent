from django.shortcuts import render
from .models import Category


def home_page(request):
    context = {
        'category' : Category.objects.root_node(tree_id=1).get_children()
    }
    return render(request, 'home/home.html', context=context)

def category(request, slug):
    context = {
        'category' : Category.objects.get(slug=slug)
    }
    return render(request, 'home/category.html', context=context)
