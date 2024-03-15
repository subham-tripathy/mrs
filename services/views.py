from datetime import datetime, timedelta
from django.shortcuts import render
from .models import YourModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def signup(request):
    if request.COOKIES.get('mrsUser'):
        return render(request, 'signup/index.html', {"msg":"alreadyloggedin"})
    else:
        if request.method == 'POST':
            try:
                user = YourModel.objects.get(username=request.POST.get('username'))
                gotUser = True
                return render(request, 'signup/index.html', {"msg":"userfound"})
            except:
                gotUser = False

            if gotUser == False:
                if request.POST.get('password') == request.POST.get('cpassword'):
                    user = YourModel.objects.create(username=request.POST.get('username'), password=request.POST.get    ('password'))
                    user.save()
                    response = render(request, 'signup/index.html', {"msg":"successsignup"})
                    expiration_date = datetime.now() + timedelta(days=1)  # Set expiration date to 1 day
                    response.set_cookie('mrsUser', request.POST.get('username'), expires=expiration_date)
                    return response
                else:
                    return render(request, 'signup/index.html', {"msg":"passwordnotsame"})
        else:
            return render(request, 'signup/index.html')



@csrf_exempt
def user_login(request):
    if request.COOKIES.get('mrsUser'):
        return render(request, 'login/index.html', {"msg":"alreadyloggedin"})
    else:
        if request.method == 'POST':
            try:
                user = YourModel.objects.get(username=request.POST.get('username'))
                gotUser = True
            except:
                gotUser = False
                return render(request, 'login/index.html', {"msg":"usernotfound"})

            if gotUser and user.password == request.POST.get('password'):
                response = render(request, 'login/index.html', {"msg":"successLogin"})
                expiration_date = datetime.now() + timedelta(days=1)  # Set expiration date to 1 day
                response.set_cookie('mrsUser', request.POST.get('username'), expires=expiration_date)
                return response
            else:
                return render(request, 'login/index.html', {"msg":"incorrectpassword"})
        else:
            return render(request, 'login/index.html')




def logout(request):
    if request.COOKIES.get('mrsUser'):
        response = render(request, 'logout/index.html', {"msg":"logoutsuccess"})
        expiration_date = datetime.now() - timedelta(days=1)
        response.set_cookie('mrsUser', request.POST.get('username'), expires=expiration_date)
        return response
    else:
        return render(request, 'logout/index.html', {"msg":"notloggedin"})