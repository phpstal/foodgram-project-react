from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import CustomUser
from .serializers import CustomUserSerializer




@api_view(['GET', 'POST'])
def CustomUserView(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)