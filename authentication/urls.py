from django.urls import path
from django.views.generic import TemplateView

from authentication.views.admin import login_admin, forgot_password
from authentication.views.common import logout_user

urlpatterns = [
    # Template view
    path('login/', TemplateView.as_view(template_name = 'authentication/admin/login_admin.html'), name='admin_login_temp'),
    path('forgot-password/', TemplateView.as_view(template_name = 'authentication/admin/forgot_password.html'), name='admin_forgot_password_temp'),

    # View
    path('login/validate/', login_admin.LoginAdmin.as_view(), name='admin_login_validate'),

    # ajax
    path('forgot-password/update/', forgot_password.ForgotPasswordAdmin.as_view(), name='admin_forgot_password'),

    # Logout
    path('logout/', logout_user.logout_view, name='logout_user'),
]