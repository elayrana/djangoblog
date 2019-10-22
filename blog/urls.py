from django.urls import path
import blog.views as views 


app_name = 'blog'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post'),
    path('post/new/',views.PostCreateView.as_view(),name='new_post'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name='delete_post'),
    
]
