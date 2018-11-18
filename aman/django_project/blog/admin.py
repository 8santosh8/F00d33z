from django.contrib import admin
from .models import Post

# This will register the models to the admin page.
admin.site.register(Post)