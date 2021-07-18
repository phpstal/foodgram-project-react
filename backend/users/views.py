from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser
from users.serializers import UserRegistrationSerializer


class UserViewSet(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)