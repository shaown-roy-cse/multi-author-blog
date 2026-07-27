from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver



# =========================
# Author Profile
# =========================

class AuthorProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    is_author = models.BooleanField(
        default=False
    )


    def __str__(self):
        return self.user.username
    # =========================
# Create Author Profile Automatically
# =========================

@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):

    if created:
        AuthorProfile.objects.create(
            user=instance,
            is_author=False
        )



# =========================
# Category
# =========================

class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )


    def __str__(self):
        return self.name



# =========================
# Tag
# =========================

class Tag(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )


    def __str__(self):
        return self.name



# =========================
# Post
# =========================

class Post(models.Model):

    STATUS_CHOICES = (

        ('draft', 'Draft'),

        ('published', 'Published'),

    )


    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    title = models.CharField(
        max_length=200
    )


    slug = models.SlugField(
        unique=True,
        blank=True
    )


    content = models.TextField()


    featured_image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True
    )


    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )


    tags = models.ManyToManyField(
        Tag,
        blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )


    view_count = models.PositiveIntegerField(
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)



    def __str__(self):

        return self.title



# =========================
# Comment
# =========================

class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )


    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    content = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):

        return self.content





# =========================
# Like
# =========================

class Like(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    class Meta:

        unique_together = (
            'post',
            'user'
        )



    def __str__(self):

        return f"{self.user.username} liked {self.post.title}"