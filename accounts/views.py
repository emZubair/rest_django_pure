from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserDetailsSerializers


class AuthView(ObtainAuthToken):
    """
    Authentication View

    :url: accounts/auth/
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Custom Authentication View

        :param request: (HttpRequest) Http Request
        :param args: argument list
        :param kwargs: keyword arguments

        :returns: (Response) Rest-framework Response
        """

        if request.user.is_authenticated:
            return Response("You are already authenticated", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': user.id, 'token': token.key, 'email': user.email}, status=status.HTTP_200_OK)


class UserDetailsAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = UserDetailsSerializers

    def get_queryset(self):

        return User.objects.filter(id=self.kwargs.get('id'))

    def get_serializer_context(self):
        return {'request': self.request}
