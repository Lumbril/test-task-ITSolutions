from rest_framework.routers import DefaultRouter
# from api import views as views_api


router = DefaultRouter(trailing_slash=False)
# router.register('account', views_api.RecoveryView, basename='recovery')

urlpatterns = router.urls