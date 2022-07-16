from django.urls import include, path
from rest_framework.routers import DefaultRouter

<<<<<<< HEAD
from .views import (CategoryViewSet, GenreViewSet, TitleViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
=======
from .views import SignUpView, UserViewSet, GetTokenView

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpView.as_view()),
    path('v1/auth/token/', GetTokenView.as_view()),
]
>>>>>>> develop
