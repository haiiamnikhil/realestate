from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from properties.models import Properties

@method_decorator(login_required, name="dispatch")
class ListPoppertiesAdmin(generic.ListView):
    template_name = 'properties/admin/list_properties.html'
    paginate_by = 15
    model = Properties

    def get_queryset(self):
        query = super().get_queryset()
        properties = query.all().order_by('-created_at')
        paginator = Paginator(properties, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        return properties