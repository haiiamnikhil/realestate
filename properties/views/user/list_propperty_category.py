from django.views import generic
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from properties.models import Properties


class ListPoppertiesByCategory(generic.ListView):
    template_name = 'properties/user/list_properties_template.html'
    paginate_by = 20
    model = Properties

    def get_queryset(self, category=None):
        query = super().get_queryset()
        filter_value = self.get_filter_value()

        if filter_value['category'] == 'recent':
            properties = query.filter(status='active').order_by('-created_at')[:10]
        else:
            properties = query.filter(**filter_value).order_by('-created_at')

        paginator = Paginator(properties, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        return properties

    def get_context_data(self):
        context = super(ListPoppertiesByCategory,self).get_context_data()
        context['category'] = self.kwargs.get('category')
        return context

    def get_filter_value(self):
        params = {}
        params['category'] = self.kwargs.get('category')
        params['status'] = 'active'
        return params