import hashlib
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, filters, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.decorators import action
from django_filters import rest_framework, CharFilter, FilterSet

from .permissions import IsAdmin, IsAuthor, IsModerator, IsReadOnly
from .models import FoodUser
from .serializers import FoodUserSerializer


class FoodUserViewSet(viewsets.ModelViewSet):
    queryset = FoodUser.objects.all()
    serializer_class = FoodUserSerializer
    permission_classes = (IsAdmin,)
    filterset_fields = ('email',)
    lookup_field = 'username'

    @action(detail=False, methods=['GET', 'PATCH'],
            permission_classes=(IsAuthenticated,))
    def me(self, request):
        user = request.user
        if request.method == 'GET' and not request.user.is_admin:
            return Response(self.get_serializer(user).data)
        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class Registration(APIView):
    permission_classes = (AllowAny,)

    def confirmation_code_generate(self, email):
        confirmation_code = hashlib.md5(
            f'{email}{settings.SECRET_KEY}'.encode('utf-8')
        ).hexdigest()
        return confirmation_code

    def send_email(self, email, message, token=None):
        if settings.EMAIL_HOST_USER:
            send_mail(
                'Регистрация в Foodgram',
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )


class GetConfirmationCode(Registration):
    def post(self, request):
        serializer = ConfirmationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        confirmation_code = self.confirmation_code_generate(email)
        message = f'Ваш код подтверждения {confirmation_code} для {email}'
        self.send_email(email, message)
        serializer.save(is_active=False, username=email)
        return Response(
            f'Код подтверждения отправлен на {email}',
            status=status.HTTP_200_OK
        )


class GetToken(Registration):
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'token': str(refresh.access_token),
        }

    def post(self, request):
        email = request.data['email']
        confirmation_code = request.data['confirmation_code']
        confirmation_code_check = self.confirmation_code_generate(email)
        if confirmation_code == confirmation_code_check:
            user = get_object_or_404(FoodUser, email=email)
            token = self.get_tokens_for_user(user)
            return Response(token, status=status.HTTP_200_OK)
        return Response(
            'Ошибка в коде или email. Получите новый код подтверждения',
            status=status.HTTP_400_BAD_REQUEST
        )