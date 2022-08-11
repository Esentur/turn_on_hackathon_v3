from django.contrib import admin

from apps.team.models import Team, Comment, Like, Favourite, Rating


class CommentInAdmin(admin.TabularInline):
    model = Comment
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'created_at']
    search_fields = ['author','text']
    list_filter = ['author']


class TeamAdmin(admin.ModelAdmin):
    inlines = [CommentInAdmin]
    list_display = ['name', 'slogan', 'captain']
    search_fields = ['name', 'slogan']
    list_filter = ['name', 'slogan', 'captain']


admin.site.register(Team, TeamAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
admin.site.register(Favourite)
admin.site.register(Rating)
