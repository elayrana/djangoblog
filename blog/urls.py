from django.urls import path
from django.contrib.auth.decorators import login_required
import blog.views as views 


app_name = 'blog'
urlpatterns = [
    path('',
        login_required(views.HomeView.as_view()),name='home'),
    path('post/<int:pk>/',
        login_required(views.PostDetailView.as_view()),name='post'),
    path('post/new/',
        login_required(views.PostCreateView.as_view()),name='new_post'),
    path('post/<int:pk>/update/',
        login_required(views.PostUpdateView.as_view()), name='update_post'),
    path('post/<int:pk>/delete/',
        login_required(views.PostDeleteView.as_view()), name='delete_post'),
    
]
