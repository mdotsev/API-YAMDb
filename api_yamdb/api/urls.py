from django.urls import include, path
from rest_framework import routers

from .views import SignUpView, UserViewSet, GetTokenView

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpView.as_view()),
    path('v1/auth/token/', GetTokenView.as_view()),
]
