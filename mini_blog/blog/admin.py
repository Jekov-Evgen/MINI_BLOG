from django.contrib import admin
from blog.models import Blog_user, Comments

@admin.register(Blog_user)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'author_name', 'publication_date']
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'to_which_post']

# Register your models here.
