from django.contrib import admin
from .models import Post, Images, Comment

class PostAdmin(admin.ModelAdmin):
	#which list you have to display on the admin page of blog 
	list_display = ('title', 'slug', 'author', 'status')
	# It is used to filter
	list_filter = ('status', 'created', 'updated')
	# enables the search box on the admin 
	search_fields = ('author__username', 'title')
	prepopulated_fields = {'slug':('title',)}
	list_editable = ('status',)
	date_hierarchy = ('created')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')



admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)

