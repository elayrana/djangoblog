from django.urls import path,include
import accounts.views as views


app_name = 'accounts'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]
