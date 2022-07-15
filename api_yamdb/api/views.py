import uuid

from django.core.mail import send_mail
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import User
from .serializers import AuthSerializer, GetTokenSerializer, UserSerializer


class SignUpView(APIView):

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data.get('username'))
            email = serializer.data.get('email')
            confirmation_code = uuid.uuid4()
            user.confirmation_code = f'{confirmation_code}'
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
            if code != user.confirmation_code:
                return Response(
                    serializer.errors, status=status.HTTP_404_NOT_FOUND
                )
            refresh = RefreshToken.for_user(user)
            access = {'access': str(refresh.access_token)}
            return Response(access, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
