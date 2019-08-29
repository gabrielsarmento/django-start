from django.urls import path
from users.views import list_users
from users.views import save_users


urlpatterns = [
    path('list/', list_users, name='list_users'),
    path('new/', save_users, name='save_users')
]
