from django.contrib import admin

# Register your models here.
from rangefilter.filters import DateRangeFilter

from BlogPosts.models import CustomUser, Post, Comment


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.user == request.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(CustomUser, CustomUserAdmin)


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    list_filter = ("title", "content", ('date_created', DateRangeFilter))

    inlines = [CommentInLine, ]

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == CustomUser.objects.get(user=request.user):
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if obj and request.user in obj.user.blocked_user.all():
            return False
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "author")

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and (obj.author == CustomUser.objects.get(user=request.user) or
                    obj.post.user == CustomUser.objects.get(user=request.user)):
            return True
        return False


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
