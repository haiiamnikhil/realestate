from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from user.models import Users
from utils.common.response.response import ResponseGenerator

response_render = ResponseGenerator()

@csrf_exempt
def fetch_user(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            user = Users.objects.get(email=email)
            response = response_render.render_response_json(redirect_url='admin_forgot_password')
            return JsonResponse(response,safe=False)

        except Exception as e:
            print(e)
            response = response_render.render_response_json(success=False,message='Invalid User')
            return JsonResponse(response, safe=False)