from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.permissions import CustomPermission
from apps.account.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, \
    ForgotPasswordCompleteSerializer, ForgotPasswordSerializer, UserSerializer
from apps.account.tasks import celery_send_info_about_activation

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return (Response('You have been successfully registered and you have been sent an '
                             'email with an activation code !', status=201))


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            celery_send_info_about_activation.delay(user.email)
            return Response({'msg': 'The activation was successful !'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Invalid code!'}, status=400)


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data,
                                               context={'request': request})

        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Password has been successfully changed !')


class ForgotPasswordView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('An email was sent to you to recover your password !')


class ForgotPasswordComplete(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Password successfully reset !')

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomPermission]
