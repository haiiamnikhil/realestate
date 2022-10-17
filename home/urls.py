from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('contact-us/', TemplateView.as_view(template_name='home/user/contact_us.html'), name='contact_us_temp'),
]