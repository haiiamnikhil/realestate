from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from properties.models import Properties
from utils.common.response.response import ResponseGenerator


response_render = ResponseGenerator()

@login_required
@csrf_exempt
def delete_prop(request):
    if request.method == 'POST':
        try:
            uid = request.POST.get('uid')
            property = Properties.objects.get(uid=uid)
            property.status = 'deleted'
            property.save()
            response = response_render.render_response_json(True, message='Property deleted')
            return JsonResponse(response, safe=False)

        except Exception as e:
            print(e)
            response = response_render.render_response_json(False, message='Something went wrong')
            return JsonResponse(response, safe=False)