from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from user.models import UserDetails
from system_settings.models import EmailSettings
from utils.common.response.response import ResponseGenerator


@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class EmailNotificationSettings(generic.CreateView):

    response_render = ResponseGenerator()

    def post(self, request, *args, **kwargs):
        value = self.extract_value(request)
        if not value['is_enabled']:
            EmailSettings.objects.update_or_create(user=value['user'],defaults={'is_enabled':value['is_enabled']})
            message = 'Email Notification disabled'
        else: 
            EmailSettings.objects.update_or_create(user=value['user'],defaults=value) 
            message = 'Email Notification enabled'
        response = self.response_render.render_response_json(success=True, message=message)
        return JsonResponse(response, safe=False)

    
    def extract_value(self,request):
        params = {}
        data = request.POST
        params['is_enabled'] = True if data.get('is_enabled') == 'on' else False
        params['user'] = UserDetails.objects.get(user=request.user)
        params['email'] = data.get('email')
        return params