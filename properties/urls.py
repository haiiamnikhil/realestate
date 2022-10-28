from django.urls import path
from django.views.generic import TemplateView

from properties.views.user import (list_properties_view, create_property_view, 
                property_details_view, search_filter_list_properties, 
                list_propperty_category, latest_properties_carousel)
from properties.views.admin import create_property
from properties.ajax.property import get_latest_properties

urlpatterns = [
    #view
    path('',list_properties_view.ListPoppertiesUser.as_view(),name='user_list_properties'),
    path('<str:category>/',list_propperty_category.ListPoppertiesByCategory.as_view(),name='user_list_properties_category'),
    path('create/',create_property.CreatePropertyAdmin.as_view(),name='user_create_property'),
    path('details/<str:slug>/<str:uid>/',property_details_view.PropertyDetailsUser.as_view(),name='user_property_details'),

    #ajax
    path('ajax/list/filter/', search_filter_list_properties.SearchFilterPropertiesUser.as_view(), name='search_filter_properties'),
    path('ajax/list/latest-prop/', latest_properties_carousel.PropertyCarousel.as_view(), name='get_latest_prop_ajax'),
]