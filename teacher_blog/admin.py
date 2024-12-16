from django.contrib import admin
from .models import Tutorial, Category

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'file', 'category',)
    list_display_links = ('title', 'text', 'file',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'category_type', 'text',)
    list_display_links = ('title', 'category_type', 'text',)

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Category, CategoryAdmin)