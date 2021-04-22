from django.urls import path
from .views import SignUp, Login, GetCharacter, GetCharacterQuote, AddFavouriteCharacter, AddFavouriteQuote

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login_user'),
    path('characters', GetCharacter.as_view(), name='get_character'),
    path('characters/<slug:id>/quotes', GetCharacterQuote.as_view(), name='get_character_quote'),
    path('characters/<slug:id>/favourites', AddFavouriteCharacter.as_view(), name='add_favourite_character'),
    path('characters/<slug:id>/quotes/<slug:qid>/favourites', AddFavouriteQuote.as_view(), name='add_favourite_character')
]

