from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.serializers import UserRegistrationSerializer, UserSerializer


class UserView(ViewSet):
    @action(detail=False, methods=['post'], url_path='registration')
    @swagger_auto_schema(
        tags=['user'],
        request_body=UserRegistrationSerializer,
        responses={
            status.HTTP_200_OK: UserSerializer
        },
        operation_id='Регистрация'
    )
    def registration(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        user = serializer.create(validated_data)

        return Response(UserSerializer(user).data)
