from django.views.generic import ListView, DetailView

from .models import Post

class PublishedPostsMixin(object):
    def get_queryset(self,):
        queryset = super(PublishedPostsMixin, self).get_queryset()
        return queryset.filter(published=True)

class PostListView(PublishedPostsMixin, ListView):
    model = Post
    
    def get_queryset(self,):
        queryset = super(PostListView, self).get_queryset()
        return queryset.filter(published=True) 

class PostDetailView(PublishedPostsMixin, DetailView):
    model = Post
    
    def get_queryset(self,):
        queryset = super(PostDetailView, self).get_queryset()
        return queryset.filter(published=True)
