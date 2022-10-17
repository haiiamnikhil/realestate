from django.views import generic
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login


@method_decorator(csrf_exempt, name="dispatch")
class LoginAdmin(generic.CreateView):
    
    def post(self, request):
        next = request.POST.get('next')
        user = self.auth_user(request)
        if user and next is not None:      
            return redirect(next)
        elif user:
            return redirect('user_list_properties')
        else:
            return redirect('admin_login_temp')


    def auth_user(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return True
        else:
            return False