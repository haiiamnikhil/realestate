from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from dashboard.views.admin import dashboard_admin
from properties.views.admin import create_property, list_properties
from user.views.admin import change_password
from notifications.views.admin import list_notificaitions, notification_details

urlpatterns = [
    # Template View
    path('admin/change-password/', login_required(TemplateView.as_view(template_name = 'dashboard/admin/change_password.html')), name='admin_change_password_temp'),

    # View
    path('admin/', dashboard_admin.DashboardView.as_view(), name='admin_dashboard_view'),
    path('admin/create/', create_property.CreatePropertyAdmin.as_view(), name='admin_create_property'),
    path('admin/properties/', list_properties.ListPoppertiesAdmin.as_view(), name='admin_list_property'),
    path('admin/notifications/', list_notificaitions.ListNotificationsAdmin.as_view(), name='admin_notifications_list'),
    path('admin/notifications/details/<str:uid>/', notification_details.NotificationDetailsAdmin.as_view(), name='admin_notifications_details'),
    
    # Ajax
    path('admin/password/update/', change_password.ChangePasswordAdmin.as_view(), name='change_password_view'),
]