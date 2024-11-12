from django.contrib import admin
from .models import Project, Task, Comment

# Register your models here.

# Remove the registration of the built-in User model
# admin.site.register(User)  # This line should be removed

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)