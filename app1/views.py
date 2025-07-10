
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomSetPasswordForm

# @login_required
def set_password(request):
    user = request.user
    form = CustomSetPasswordForm(user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        user.requires_password_change = False
        user.save()
        return redirect('dashboard')
    return render(request, 'set_password.html', {'form': form})



def login(request):
    return render (request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')