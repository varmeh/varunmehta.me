from django.views.generic import ListView, DetailView
from models import Blog, Tag
from django.core.cache import cache

# Create your views here.
class BlogList(ListView):
    template_name = 'blog_list.html'
    queryset = Blog.objects.all().order_by('-published_on')
    context_object_name = 'blogs'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().order_by('title')
        return context

#Detailed Blog View with Comment
class BlogDetail(DetailView):
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    queryset = Blog.objects.all()

    def get_object(self, queryset=queryset):
        return super(BlogDetail, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().order_by('title')
        return context

#Blog Attached to Tag
# class TagBlogList(ListView):
#     template_name = 'blog_list.html'
#     context_object_name = 'blogs'
#     paginate_by = 3
#
#     def get_context_data(self, **kwargs):
#         context = super(TagBlogList, self).get_context_data(**kwargs)
#         context['tags'] = Tag.objects.all().order_by('title')
#         return context
#
#     def get_queryset(self):
#         return Blog.objects.filter(tags__slug=self.kwargs.get('slug'))

class TagBlogList(BlogList):
    template_name = 'tag_list.html'

    def get_context_data(self, **kwargs):
        context = super(TagBlogList, self).get_context_data(**kwargs)
        context['tag_title'] = Tag.objects.get(slug=self.kwargs['slug']).title
        return context

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get('slug'))

def get_footer_context():
    pass