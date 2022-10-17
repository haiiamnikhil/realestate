from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from properties.models import Properties, PropertyImages
from user.models import UserDetails
from utils.common.response.response import ResponseGenerator

@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class CreatePropertyAdmin(generic.CreateView):
    template_name = 'properties/admin/create_property.html'
    response_render = ResponseGenerator()

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        values = self.extract_values(request)
        try:
            property = Properties.objects.create(**values)
            files = request.FILES.getlist('image')
            if len(files) > 0:
                add_file = self.add_prop_file(property,files)
            response = self.response_render.render_response_json(True,redirect_url='user_list_properties')
            return JsonResponse(response,safe=False)
        except Exception as e:
            print(e)
            response = self.response_render.render_response_json(False,message='Something went wrong')
            return JsonResponse(response,safe=False)

    def extract_values(self, request):
        params = {}
        data = request.POST

        for key, value in data.items():
            params[key] = value

        params['user'] = UserDetails.objects.get(user=request.user)
        return params

    def add_prop_file(self,property,files):
        for image in files:
            property_image = PropertyImages()
            property_image.property=property
            property_image.image=image
            property_image.save()
