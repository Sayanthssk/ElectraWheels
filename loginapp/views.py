from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
import json
from django.contrib.auth import login

from .models import Userprofile, Token

# Create your views here.
class UserLogin(View):
    template_name ="login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
                        "ADMIN": "admindashboard",
                        "RESTAURANT":"rest",
                        "CAMP":"camp",
                        "USER":"user:loadteacher",
                    }
        username = request.POST.get("username")
        password = request.POST.get("password")
        authenticated = authenticate(username=username, password=password)
        try:
            user = Userprofile.objects.get(username=username)
            print("hel")
            print(user.status)
        except Userprofile.DoesNotExist:
            response_dict[
                            "reason"
                        ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])

        if user.status == 'DEACTIVE':
            print(user.status)
            response_dict["reason"] = "Contact admin account not verified."
            messages.error(request, response_dict["reason"])
            return HttpResponse('''<script>alert("Contact admin account not verified"); window.location.href="/login/";</script>''')
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return HttpResponse('''<script>alert("Invalid credentials"); window.location.href="/login/";</script>''')


        else:
            print("hello")
            session_dict = {"real_user": authenticated.id}
            request.session["user_id"] = authenticated.id 
            token, c = Token.objects.get_or_create(
                        user=user, defaults={"session_dict": json.dumps(session_dict)}
                        )

    

            user_type = authenticated.user_type
            user_id=authenticated.id
            




            print("hai")
            print(user)
            print(user_type)
            print(user_id)

            return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or loadlogin)
    
    
class Admin_dashboard(View):
        def get(self,request):
            return render(request, 'admin_dashboard.html')
        
