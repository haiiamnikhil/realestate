from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from properties.models import Properties, PropertyImages


@method_decorator(csrf_exempt, name="dispatch")
class CreatePropertyUser(generic.CreateView):
    template_name = 'properties/user/create_property.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        values = self.extract_values(request)
        try:
            property = Properties.objects.create(**values)
            files = request.FILES.getlist('image')
            if len(files) > 0:
                add_file = self.add_prop_file(property,files) 
            return JsonResponse({'success':True},safe=False,status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'success':False},safe=False,status=200)

    def extract_values(self, request):
        params = {}
        data = request.POST
        files = request.FILES.getlist('image')

        for key, value in data.items():
            params[key] = value

        return params

    def add_prop_file(self,property,files):
        for image in files:
            property_image = PropertyImages()
            property_image.property=property
            property_image.image=image
            property_image.save()
