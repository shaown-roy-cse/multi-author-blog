from django.urls import path
from . import views


from django.urls import path
from . import views


urlpatterns = [

    # Home
    path(
        '',
        views.home,
        name='home'
    ),


    # Authentication

    path(
        'register/',
        views.register,
        name='register'
    ),


    path(
        'login/',
        views.login_view,
        name='login'
    ),


    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),



    # Profile

    path(
        'profile/',
        views.profile,
        name='profile'
    ),


    path(
        'edit-profile/',
        views.edit_profile,
        name='edit_profile'
    ),



    # Public Author Profile

    path(
        'author/<str:username>/',
        views.author_profile,
        name='author_profile'
    ),




    # Author Dashboard

    path(
        'author-dashboard/',
        views.author_dashboard,
        name='author_dashboard'
    ),




    # Posts

    path(
        'posts/',
        views.post_list,
        name='post_list'
    ),



    path(
        'posts/<int:id>/',
        views.post_detail,
        name='post_detail'
    ),



    path(
        'create-post/',
        views.create_post,
        name='create_post'
    ),



    path(
        'posts/<int:id>/edit/',
        views.edit_post,
        name='edit_post'
    ),



    path(
        'posts/<int:id>/delete/',
        views.delete_post,
        name='delete_post'
    ),



    path(
        'posts/<int:id>/publish/',
        views.publish_post,
        name='publish_post'
    ),



    path(
        'posts/<int:id>/unpublish/',
        views.unpublish_post,
        name='unpublish_post'
    ),




    # Comments

    path(
        'posts/<int:id>/comment/',
        views.add_comment,
        name='add_comment'
    ),



    path(
        'comments/<int:id>/edit/',
        views.edit_comment,
        name='edit_comment'
    ),



    path(
        'comments/<int:id>/delete/',
        views.delete_comment,
        name='delete_comment'
    ),




    # Like

    path(
        'posts/<int:id>/like/',
        views.like_post,
        name='like_post'
    ),


]