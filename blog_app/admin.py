from django.contrib import admin
from blog_app.models import Blog, Tag
# Register your models here.

class TextAreaAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'tinymce/tinymce.min.js',
            'tinymce/textarea.js',
        )

class BlogAdmin(TextAreaAdmin):
    #As created and modified fields are automatically generated, they are not editable and thus, would not be displayed
    # as a part of editable fields section.
    fields = ['title', 'body', 'published', 'slug', 'tags']
    date_hierarchy = 'published_on'
    prepopulated_fields = { 'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
