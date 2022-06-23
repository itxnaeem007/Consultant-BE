from django.contrib import admin
from blog.models import Author,Comment,Post
from django.contrib.auth.models import Group

admin.site.site_header = "CH-Consultancy"
admin.site.site_title = "CH-Consultancy Admin Panel"
admin.site.index_title = "Welcome to Portal"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','overview','timestamp')
    list_filter = ('timestamp',)


admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post,PostAdmin)
admin.site.unregister(Group)
