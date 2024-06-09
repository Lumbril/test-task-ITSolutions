from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, mixins

from api.models import Announcement
from api.serializers import AnnouncementSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['announcement'],
    responses={
        status.HTTP_200_OK: AnnouncementSerializer
    },
    operation_id='Получить список объявлений'
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    tags=['announcement'],
    responses={
        status.HTTP_200_OK: AnnouncementSerializer
    },
    operation_id='Получить объявление по id'
))
class AnnouncementView(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       GenericViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'id_announcement'
    permission_classes = [IsAuthenticated]
