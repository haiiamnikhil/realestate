from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from user.models import UserDetails
from utils.common.response.response import ResponseGenerator


@method_decorator(csrf_exempt, name="dispatch")
class UpdateUserDetails(generic.CreateView):

    response_render = ResponseGenerator()
    
    def post(self, request):
        data = self.extract_values(request.POST)
        try:
            user = UserDetails.objects.get(uid=data['uid'])
            if user:
                UserDetails.objects.update_or_create(uid=data['uid'],defaults=data)
                response = self.response_render.render_response_json(True,message='Updated user details',redirect_url='admin_dashboard_view')
                return JsonResponse(response, safe=False)
            else:
                return JsonResponse({'success':False,'message':'No User with this name'}, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'success':False, 'message':'All fields are necessary'}, safe=False)

    def extract_values(self, data):
        params = {}
        for key, value in data.items():
            params[key] = value

        return params