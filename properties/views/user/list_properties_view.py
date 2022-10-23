from django.views import generic
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from properties.models import Properties


class ListPoppertiesUser(generic.ListView):
    template_name = 'properties/user/list_properties_template.html'
    paginate_by = 20
    model = Properties

    def get_queryset(self):
        query = super().get_queryset()
        properties = query.filter(status='active').order_by('-created_at')
        search = self.get_search_params()
        if search:
            properties = query.filter(**search)

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
        context = super(ListPoppertiesUser,self).get_context_data()
        context['search'] = self.get_search_params()
        return context

    def get_search_params(self):
        params = {}
        value = self.request.GET
        for key, value in value.items():
            if value == 'all' or key == 'page':
                pass
            elif key == 'search':
                params['heading__icontains'] = value
            else:
                params[key] = value

        return params