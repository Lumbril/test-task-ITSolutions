from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.serializers import *


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        tags=['user'],
        request_body=UserLoginSerializer,
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        },
        operation_id='Создать access и refresh токены'
    )
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        return data


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

    @swagger_auto_schema(
        tags=['user'],
        request_body=CustomTokenRefreshSerializer,
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        },
        operation_id='Обновить токен'
    )
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        return data


