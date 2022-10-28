from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from utils.common.response.response import ResponseGenerator
from user.models import GuestUsers
from notifications.models import Notifications
from properties.models import Properties
from notifications.views.common.email_notifier import EmailNotifier
from system_settings.models import EmailSettings


@method_decorator(csrf_exempt, name='dispatch')
class SendMessageUser(generic.CreateView):

    response_render = ResponseGenerator()
    email_notifier = EmailNotifier()
    
    def post(self, request):
        data = self.extract_values(request)
        user = request.user
        try:
            guest = GuestUsers()
            guest.full_name = data['full_name']
            guest.email = data['email']
            guest.phone = data['phone']
            guest.save()
            notification = Notifications()
            notification.user = guest
            notification.comment = data['comment']
            notification.property = Properties.objects.get(uid=data['prop_uid'])
            notification.save()
            email_notify = self.email_notifier.send_email_notification(data, user, 'enquiry')
            response = self.response_render.render_response_json(message='Message send successfully')
            return JsonResponse(response, status=200)
        
        except Exception as e:
            print(e)
            response = self.response_render.render_response_json(success=False, message='Something went wrong. Please try again later')
            return JsonResponse(response, status=200)

    def extract_values(self, request):
        data = request.POST
        params = {}
        for key, value in data.items():
            params[key] = value

        return params