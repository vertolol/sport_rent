from django.shortcuts import render
from .models import Category
from django.views.generic import View, ListView, DetailView


class HomePage(ListView):

    model = Category
    template_name = 'home/home.html'
    context_object_name = 'category'

    def get_queryset(self):
        return Category.objects.root_node(tree_id=1).get_children()


class CategoryDetail(DetailView):
    model = Category
    template_name = 'home/category.html'
    context_object_name = 'category'


