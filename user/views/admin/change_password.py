from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from user.models import Users

@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class ChangePasswordAdmin(generic.CreateView):

    def post(self, request):
        try:
            data = self.extract_value(request)

            user = Users.objects.get(uid=data['uid'])
            old_password = data['old_password']
            new_password = data['new_password']
            confirm_password = data['confirm_password']
            
            is_old_password_correct = user.check_password(old_password)
            if is_old_password_correct:
                if old_password == new_password:
                    return JsonResponse({'success':False,'message':'Old and new passwords cant be the same'},safe=False)

                if old_password and new_password and new_password == confirm_password:
                    print(new_password)
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, request.user)
                    return JsonResponse({'success':True,'message':'Password updated'},safe=False)
                else:
                    return JsonResponse({'success':False,'message':'Passwords doesnot match'},safe=False)

            else:
                return JsonResponse({'success':False,'message':'Entered password is wrong'},safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'success':False,'message':'Some fields are missing'},safe=False)

    def extract_value(self, request):
        params = {}
        data = request.POST
        for key, value in data.items():
            params[key] = value

        return params
