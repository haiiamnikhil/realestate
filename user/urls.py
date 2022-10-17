from django.urls import path
from django.views.generic import TemplateView

from user.views.common import update_user_details
from user.ajax.user_ajax import fetch_user

urlpatterns = [
    # view
    path('update/details/', update_user_details.UpdateUserDetails.as_view(), name='update_user_details'),

    # ajax
    path('get-user/', fetch_user, name='fetch_user_ajax')
]