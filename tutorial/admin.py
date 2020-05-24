from django.contrib import admin
from .models import Tutorial, Category, Tag
admin.site.register(Tutorial)
admin.site.register(Category)
admin.site.register(Tag)