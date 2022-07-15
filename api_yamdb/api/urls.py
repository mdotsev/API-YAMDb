from django.urls import include, path
from rest_framework import routers
# from rest_framework_simplejwt.views import TokenObtainPairView

from .views import SignUpView, UserViewSet, GetTokenView

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', SignUpView.as_view()),
    path('auth/token/', GetTokenView.as_view()),
]
