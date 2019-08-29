from django.shortcuts import render, redirect
from users.forms import UserForm
from users.models import User


def list_users(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})

def save_users(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    return render(request, 'user_form.html', {'form': form})
