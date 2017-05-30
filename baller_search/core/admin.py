from django.contrib import admin

from .models import Post, NerdBaller


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'nerdballer', 'score', 'pub_date')
    ordering = ('-score',)
    search_fields = ('title', 'nerdballer__username', 'nerdballer__known_as')


class NerdBallerAdmin(admin.ModelAdmin):
    list_display = ('username', 'known_as')
    ordering = ("username", )
    search_fields = ('username', 'known_as')


admin.site.register(Post, PostAdmin)
admin.site.register(NerdBaller, NerdBallerAdmin)
