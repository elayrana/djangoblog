from django.urls import path
import blog.views as views 


app_name = 'blog'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post'),
]
