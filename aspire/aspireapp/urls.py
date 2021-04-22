from django.urls import path
from .views import SignUp, Login, GetCharacter

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login_user'),
    path('character', GetCharacter.as_view(), name='get_character')
]

