from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views as views_api


router = DefaultRouter(trailing_slash=False)
router.register('announcement', views_api.AnnouncementView, basename='recovery')
router.register('user', views_api.UserView, basename='user')

additional_urlpatterns = [
    path('user/authenticate', views_api.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/reissueJwt', views_api.CustomTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = router.urls + additional_urlpatterns
