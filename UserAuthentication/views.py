from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST.get("UserName")
        userpwd = request.POST.get("UserPWD")
        # user1 = auth.User.objects.get(username = username)
        # print(user1)
        user = auth.authenticate(username = username,password = userpwd)
        # print(user)
        if(user):
            auth.login(request, user)
            print("登录成功")
            # print(user.username)
            # return render(request, "Index.html", {'user': user.username})
            return redirect('/Index')
        else:
            return render(request, 'Login.html')
    else:
        print('2222')
        return render(request, "Login.html")

def index(request):
    print("进入index")
    if request.user.is_authenticated:
        name = request.user.username
        print(name)
        return render(request, "index.html", {'user': name})
    else:
        return render(request, "Login.html")

def Regist(request):
    print("00")
    if request.method == 'POST':
        print("111")
        username = request.POST.get("UserName")
        print(username)
        userpwd = request.POST.get("UserPWD")
        user = User.objects.create_user(username, userpwd, '123456789')
        user.last_name = "test"
        user.first_name = "t"
        user.save()
        return render(request, "Login.html")
    else:
        print("222")
        return render(request, "regist.html")

def Logoff(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/Login')

