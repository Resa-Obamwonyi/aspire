from django.db import transaction
from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

from .models import User, FavQuote, FavCharacter
from . import serializers
from .lib.lower_strip import strip_and_lower
import requests as Req
from decouple import config

one_api_url = config('API_BASE_URL')
api_token = config('API_TOKEN')


# SignUp View
class SignUp(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        with transaction.atomic():

            if not (request.data.get('username', '') or len(request.data.get('username', '') > 3)):
                return Response(
                    dict(error='Invalid Username, Username must be at least three Characters long.'),
                    status=status.HTTP_400_BAD_REQUEST)

            user_data = {
                "username": request.data["username"],
                "email": request.data["email"],
                "password": request.data["password"]
            }

            user_serializer = serializers.UserSerializer(data=user_data)

            if user_serializer.is_valid():
                user = user_serializer.save()
                user.set_password(request.data["password"])

                return Response(
                    dict(success='Your account has been created successfully.'),
                    status=status.HTTP_201_CREATED)
            else:
                return Response(
                    user_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


# Login View
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = strip_and_lower(request.data.get('email', ''))
            password = request.data.get('password', '')

            if email is None or password is None:
                return Response(
                    dict(invalid_credential='Please provide both email and password'),
                    status=status.HTTP_400_BAD_REQUEST)
            try:
                db_user = User.objects.get(email=email)
            except Exception:
                return Response(
                    dict(invalid_credential='This user does not exist in our records'),
                    status=status.HTTP_400_BAD_REQUEST)

            user = check_password(password, db_user.password)

            if not user:
                return Response(
                    dict(invalid_credential='Please ensure that your email and password are correct'),
                    status=status.HTTP_400_BAD_REQUEST)

            token, _ = Token.objects.get_or_create(user=db_user)
            return Response(dict(token=token.key), status=status.HTTP_200_OK)

        except Exception as err:
            return Response(dict(error=err), status=status.HTTP_400_BAD_REQUEST)


# Get all Characters
class GetCharacter(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.id
        if user:
            get_characters = Req.get(one_api_url + '/character', headers={'Authorization': api_token})
            return Response(get_characters.json(), status=status.HTTP_200_OK)


# Get all quotes from a specific Character
class GetCharacterQuote(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = request.user.id
        if user:
            get_character_quotes = Req.get(one_api_url + '/character/' + id + '/quote',
                                           headers={'Authorization': api_token})
            quotes = get_character_quotes.json()["docs"]
            return Response(dict(Quotes=quotes), status=status.HTTP_200_OK)


# Add Favourite Character to Database
class AddFavouriteCharacter(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        user = request.user.id
        # get character
        get_character = Req.get(one_api_url + '/character/' + id, headers={'Authorization': api_token})
        character_info = get_character.json()["docs"][0]

        # Get favorite characters and check if it exsists there already
        favourite_characters = FavCharacter.objects.filter(user_id=user)

        for fav_char in favourite_characters.all():
            if fav_char.character_id == id:
                return Response(
                    dict(failure=character_info["name"] + ' already exists in Favourites.'),
                    status=status.HTTP_400_BAD_REQUEST)

        character_data = {
            "user_id": request.user.id,
            "character_id": character_info["_id"],
            "character_name": character_info["name"],
            "character_gender": character_info["gender"],
            "character_race": character_info["race"]
        }

        fav_character_serializer = serializers.FavCharacterSerializer(data=character_data)

        if fav_character_serializer.is_valid():
            fav_character = fav_character_serializer.save()

            return Response(
                dict(success=character_info["name"] + ' has been added to Favourites.'),
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                fav_character_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


# Add Favourite Quote by a Character to Database
class AddFavouriteQuote(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id, qid):
        user = request.user.id

        # get character
        get_quote = Req.get(one_api_url + '/quote/' + qid, headers={'Authorization': api_token})
        quote_info = get_quote.json()["docs"][0]
        character = Req.get(one_api_url + '/character/' + id, headers={'Authorization': api_token})
        character_info = character.json()["docs"][0]

        # Get favorite quotes and check if it exists there already
        favourite_quotes = FavQuote.objects.filter(user_id=user)

        for fav_qu in favourite_quotes.all():
            if fav_qu.quote_id == qid:
                return Response(
                    dict(failure='This Quote already exists in Favourites.'),
                    status=status.HTTP_400_BAD_REQUEST)

        quote_data = {
            "user_id": request.user.id,
            "character_id": quote_info["character"],
            "character_name": character_info["name"],
            "quote_id": quote_info["_id"],
            "quote_dialog": quote_info["dialog"],
        }

        fav_quote_serializer = serializers.FavQuoteSerializer(data=quote_data)

        if fav_quote_serializer.is_valid():
            fav_quote = fav_quote_serializer.save()

            return Response(
                dict(success='Quote has been added to Favourites.'),
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                fav_quote_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


# Get All Favourites
class Favourites(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.id

        # Get all wallets that belong to the user
        favourite_quotes = FavQuote.objects.filter(user_id=user)
        quotes = []
        for fav in favourite_quotes.all():
            quotes.append(("Character: " + fav.character_name,
                               "Dialog: " + fav.quote_dialog))

        characters = []

        favourite_characters = FavCharacter.objects.filter(user_id=user)
        for fav in favourite_characters:
            characters.append(("Character: " + fav.character_name,
                               "Gender: " + fav.character_gender,
                               "Race: " + fav.character_race))

        favourites = {
            "Quotes":quotes,
            "Characters":characters
        }

        return Response(
            dict(Favourites=favourites),
            status=status.HTTP_200_OK
        )
