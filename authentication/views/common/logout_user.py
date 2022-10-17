from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def logout_view(request):
    if request.user:
        logout(request)
        return HttpResponseRedirect(reverse('admin_login_temp'))
    else:
        return HttpResponseRedirect(reverse('admin_login_temp'))