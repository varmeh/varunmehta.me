from django.views.generic import ListView, DetailView, TemplateView
from models import Blog, Tag
from django.db.models import Count
# from django.core.cache import cache

#Creating footer Mixin
class Footer(object):

    def data(self):
        footer = {}
        queryset = Blog.objects.all().filter(published=True)
        footer['blog_count'] = queryset.count()
        footer['recent_blog'] = queryset[:3]    #top 3 blogs
        footer['tags'] = Tag.objects.annotate(Count('blog')).order_by('title')
        return footer

# Create your views here.
class BlogList(Footer, ListView):
    template_name = 'blog_list.html'
    queryset = Blog.objects.all().filter(published='True').order_by('-published_on')
    context_object_name = 'blogs'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['footer'] = self.data()
        return context

#Detailed Blog View with Comment
class BlogDetail(DetailView, Footer):
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    queryset = Blog.objects.all().filter(published='True')

    def get_object(self, queryset=queryset):
        return super(BlogDetail, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['footer'] = self.data()
        return context

#Blog Attached to Tag
class TagBlogList(BlogList):
    template_name = 'tag_list.html'

    def get_context_data(self, **kwargs):
        context = super(TagBlogList, self).get_context_data(**kwargs)
        context['tag_title'] = Tag.objects.get(slug=self.kwargs['slug']).title
        return context

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get('slug')).filter(published='True')

#About View
class About(Footer, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['footer'] = self.data()
        return context