from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from user.models import Users
from utils.common.response.response import ResponseGenerator


@method_decorator(csrf_exempt, name="dispatch")
class ForgotPasswordAdmin(generic.CreateView):

    response_render = ResponseGenerator()
    
    def post(self, request):
        params = request.POST
        user = Users.objects.get(email=params.get('email'))
        new_password = params.get('new_password')
        user.set_password(new_password)
        user.save()
        response = self.response_render.render_response_json(message='password_updated',redirect_url='admin_login_temp')
        return JsonResponse(response, safe=False)
