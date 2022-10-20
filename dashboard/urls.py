from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from dashboard.views.admin import dashboard_admin
from properties.views.admin import create_property, edit_property, list_properties
from user.views.admin import change_password
from notifications.views.admin import list_notificaitions, notification_details
from properties.ajax.property import delete_prop

urlpatterns = [
    # Template View
    path('admin/change-password/', login_required(TemplateView.as_view(template_name = 'user/admin/change_password.html')), name='admin_change_password_temp'),

    # View
    path('admin/', dashboard_admin.DashboardView.as_view(), name='admin_dashboard_view'),

    path('admin/properties/', list_properties.ListPoppertiesAdmin.as_view(), name='admin_list_property'),
    path('admin/properties/create/', create_property.CreatePropertyAdmin.as_view(), name='admin_create_property'),
    path('admin/properties/edit/<str:uid>/', edit_property.EditPropertiesAdmin.as_view(), name='admin_edit_property'),

    path('admin/notifications/', list_notificaitions.ListNotificationsAdmin.as_view(), name='admin_notifications_list'),
    path('admin/notifications/details/<str:uid>/', notification_details.NotificationDetailsAdmin.as_view(), name='admin_notifications_details'),

    path('admin/settings/', login_required(TemplateView.as_view(template_name='system_settings/admin/settings.html')), name='admin_settings'),
    
    # Ajax
    path('admin/password/update/', change_password.ChangePasswordAdmin.as_view(), name='change_password_view'),
    path('ajax/prop/status/', delete_prop, name='delete_prop_ajax'),
]