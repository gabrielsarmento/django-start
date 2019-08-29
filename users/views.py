from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserForm
from users.models import User


def list_users(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})


def save_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    return render(request, 'user_form.html', {'form': form})


def update_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    return render(request, 'user_form.html', {'form': form})


def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return redirect('list_users')
