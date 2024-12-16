from django.shortcuts import render, redirect
from .models import Tutorial, Category
from django.db.models.functions import Lower
from django.views.generic import CreateView, TemplateView, View, ListView, DetailView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from .forms import CategoryCreateForm, TutorialCreateForm, CategoryUpdateForm
from django.db.models import Q
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, "teacher_blog/index.html", context={'categories': Category.objects.all()})

"""Categories"""

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'teacher_blog/category.html'

    def get(self, request, *args, **kwargs):
        if self.get_object().category_type == 'tutorials' and not request.user.is_authenticated:
            url = reverse_lazy('list-tutorial', kwargs={'pk': self.kwargs['pk']})
            return redirect(url)

        return super().get(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'teacher_blog/category-update.html'

    def get_success_url(self):
        return self.get_object().get_absolute_url()


class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return reverse_lazy('index')


class CategoryCreateView(CreateView):
    template_name = 'teacher_blog/category-create.html'
    model = Category
    form_class = CategoryCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent = self.request.GET.get('parent', '')
        if parent:
            context['parent'] = parent
        return context
    
    def form_valid(self, form):
        return_to = self.request.POST.get('return_to')
        if return_to:
            self.object = form.save()
            return redirect('index')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')

"""Tutorials"""

class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = "teacher_blog/tutorials/detail.html"
    context_object_name = 'tutorial'
    
    def get_object(self, queryset = ...):
        pkt = self.kwargs['pkt']
        return get_object_or_404(Tutorial, pk=pkt)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object().category
        context['tutorials'] = self.get_object().get_other_tutorials()
        return context


class TutorialUpdateView(UpdateView):
    model = Tutorial
    fields = ["title", 'text']
    template_name = 'teacher_blog/tutorials/update.html'
    context_object_name = 'tutorial'
    
    def get_object(self, queryset = ...):
        pk = self.kwargs['pkt']
        return get_object_or_404(Tutorial, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object().category
        context['tutorials'] = self.get_object().get_other_tutorials()
        return context


class TutorialListView(ListView):
    model = Tutorial
    template_name = "teacher_blog/tutorials/base-list.html"
    context_object_name = 'tutorials'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Tutorial.objects.filter(category__pk=pk)
    
    def get_category(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Category, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
        return context


class TutorialDeleteView(DeleteView):
    model = Tutorial

    def get_object(self, queryset = ...):
        pk = self.kwargs['pkt']
        return get_object_or_404(Tutorial, pk=pk)

    def get_success_url(self):
        return reverse_lazy('list-tutorial', kwargs={'pk': self.kwargs['pk']})


class TutorialCreateView(CreateView):
    template_name = 'teacher_blog/tutorials/create.html'
    model = Tutorial
    form_class = TutorialCreateForm

    def get_category(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Category, pk=pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
        context['tutorials'] = self.get_category().tutorial.all()
        return context

"""Search"""

class SearchTemplateView(TemplateView):
    template_name = 'teacher_blog/search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '').lower()
        tutorials = Tutorial.objects.annotate(low_title=Lower('title'), low_text=Lower('text'))

        result = tutorials.filter(Q(low_title__icontains=query) | Q(low_text__icontains=query))

        return render(request, self.template_name, {'result': result, 'query': query,})
