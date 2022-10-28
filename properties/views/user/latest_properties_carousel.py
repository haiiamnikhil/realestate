from django.views import View
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

from properties.models import Properties
from utils.common.response.response import ResponseGenerator

class PropertyCarousel(View):
    template_name = 'properties/user/property_carousel.html'
    response_render = ResponseGenerator()

    def get(self, request, *args, **kwargs):
        try:
            properties = Properties.objects.filter(status='active').order_by('-created_at')[:10]
            data = render_to_string(self.template_name, {'properties':properties})
            resposne = self.response_render.render_response_json(success=True,template_render=data)
            return JsonResponse(resposne, safe=False)
        except Exception as e:
            print(e)
            print("sdfsdfsdfsdfsdfsdfsds")
            resposne = self.response_render.render_response_json(success=False,message='Something Went wrong')
            return JsonResponse(resposne, safe=False)