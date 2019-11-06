from django.contrib.auth.views import PasswordChangeView, TemplateView
from django.views.generic import View
from django.urls import path,include
from django.urls import reverse_lazy
import accounts.views as views


app_name = 'accounts'
urlpatterns = [
    
    path('change_password/',PasswordChangeView.as_view(success_url=
                                reverse_lazy('accounts:change_password_done'),
                                template_name='registration/change_password.html'),
                                name='change_password'),
    path('change_password/done',TemplateView.as_view(
        template_name='registration/change_password_done.html'),
        name='change_password_done'),
    path('',include('django.contrib.auth.urls')),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]
