from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class UserLoginViewSet(viewsets.ViewSet):
    def create(self, request):
        obtain_token_view = ObtainAuthToken()
        response = obtain_token_view.post(request)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})
    
class UserLogoutViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)