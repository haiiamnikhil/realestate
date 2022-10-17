from django.urls import path
from django.views.generic import TemplateView

from properties.views.user import list_properties_view, create_property_view, property_details_view, search_filter_list_properties
from properties.views.admin import create_property

urlpatterns = [
    #view
    path('',list_properties_view.ListPoppertiesUser.as_view(),name='user_list_properties'),
    path('create/',create_property.CreatePropertyAdmin.as_view(),name='user_create_property'),
    path('details/<str:slug>/<str:uid>/',property_details_view.PropertyDetailsUser.as_view(),name='user_property_details'),

    #ajax
    path('ajax/list/filter/', search_filter_list_properties.SearchFilterPropertiesUser.as_view(), name='search_filter_properties'),
]