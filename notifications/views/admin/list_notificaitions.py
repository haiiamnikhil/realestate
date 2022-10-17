from django.views import generic
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from notifications.models import Notifications


@method_decorator(login_required,name='dispatch')
class ListNotificationsAdmin(generic.ListView):
    template_name = 'notifications/admin/list_notifications.html'
    model = Notifications
    paginate_by = 10

    def get_queryset(self):
        comment = super().get_queryset().order_by('-created_at')
        paginator = Paginator(comment, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        return comment