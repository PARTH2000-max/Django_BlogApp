from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name="myapp"),
    path('about',views.about,name="myapp1"),
    path('register',views.register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('post_blog',views.user_blog,name="post_blog"),
    path('blog_detail/<int:id>',views.blog_detail,name="blog_detail"),
    path('blog_delete/<int:id>',views.delete,name="blog_delete"),
    path('blog_edit/<int:id>',views.edit,name="blog_edit"),
]
