from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, "home.html", {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['publication_date']

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context["categories_menu"] = categories_menu
        return context


def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, "category_list.html", {'category_menu_list': category_menu_list})


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, "categories.html", {'categories': categories.title().replace('-', ' '), 'category_posts': category_posts})


class PostDetailsView(DetailView):
    model = Post
    template_name = "post_details.html"

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(PostDetailsView, self).get_context_data()
        context["categories_menu"] = categories_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
