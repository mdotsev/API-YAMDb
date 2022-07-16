import uuid

from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import Category, Genre, Review, Title, User

from .mixins import ListCreateDestroyViewSet
from .permissions import IsAdminOrReadOnly
from .serializers import (
    AuthSerializer, CategorySerializer, GenreSerializer, GetTokenSerializer,
    ReadOnlyTitleSerializer, TitleSerializer, UserSerializer,
)


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(
        Avg('reviews__score')
    ).order_by('name')
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ReadOnlyTitleSerializer
        return TitleSerializer


class SignUpView(APIView):

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data.get('username'))
            email = serializer.data.get('email')
            confirmation_code = uuid.uuid4()
            user.confirmation_code = make_password(confirmation_code)
            print(user.confirmation_code)
            user.save()

            send_mail(
                'Your confirmation_code',
                f'Ваш confirmation_code: {confirmation_code}',
                'manager@yamdb.com',
                [f'{email}'],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTokenView(APIView):

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.data.get('username'))
            code = serializer.data.get('confirmation_code')
            if not check_password(code, user.confirmation_code):
                return Response(
                    'Пользователь с таким именем и кодом не найден',
                    status=status.HTTP_404_NOT_FOUND,
                )
            refresh = RefreshToken.for_user(user)
            access = {'access': str(refresh.access_token)}
            return Response(access, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
