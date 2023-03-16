from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def uhome(request):
    if request.user.is_authenticated:
        return redirect('uwelcome')
    else:
        if request.method == 'POST':
            un = request.POST.get('un')
            pw = request.POST.get('pw')
            usr = authenticate(username=un,password=pw)
            if usr is None:
                return render(request,'uhome.html',{'msg':'Invalid Credentials'})
            else:
                login(request,usr)
                return render(request,'uwelcome.html')
        else:
            return render(request,'uhome.html')
    
def usignup(request):
    if request.user.is_authenticated:
        return redirect('uwelcome')
    else:
        if request.method == 'POST':
            un = request.POST.get('un')
            pw1 = request.POST.get('pw1')
            pw2 = request.POST.get('pw2')
            if pw1 == pw2:
                try:
                    usr = User.objects.get(username=un)
                    return render(request,'usignup.html',{'msg':'User Already Exists'})
                except User.DoesNotExist:
                    usr = User.objects.create_user(username=un,password=pw1)
                    usr.save()
                    return redirect('uhome')
            else:
                return render(request,'usignup.html',{'msg':'Passwords Do Not Match'})
        else:
            return render(request,'usignup.html')
    
def uwelcome(request):
    if request.user.is_authenticated:
        return render(request,'uwelcome.html')
    else:
        return redirect('uhome')

def ulogout(request):
    logout(request)
    return redirect('uhome')
