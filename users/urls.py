from django.urls import path
from users.views import list_users
from users.views import save_user
from users.views import update_user
from users.views import delete_user


urlpatterns = [
    path('list/', list_users, name='list_users'),
    path('new/', save_user, name='save_user'),
    path('update/<int:id>/', update_user, name='update_user'),
    path('delete/<int:id>/', delete_user, name='delete_user')
]
