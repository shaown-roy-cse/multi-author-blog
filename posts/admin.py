from django.contrib import admin

from .models import (
    Post,
    Comment,
    Like,
    Category,
    Tag,
    AuthorProfile
)



# =========================
# Category Admin
# =========================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )



# =========================
# Tag Admin
# =========================

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )



# =========================
# Author Profile Admin
# =========================

@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'is_author',
    )

    list_filter = (
        'is_author',
    )



# =========================
# Post Admin
# =========================

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'category',
        'status',
        'view_count',
        'created_at',
    )


    list_filter = (
        'status',
        'category',
    )


    search_fields = (
        'title',
        'content',
    )



# =========================
# Comment Admin
# =========================

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'post',
        'author',
        'created_at',
    )



# =========================
# Like Admin
# =========================

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'post',
        'user',
        'created_at',
    )