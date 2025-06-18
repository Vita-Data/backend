from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import CustomUser
from .serializers import RegisterSerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_user(request):
    if request.user.role != 'ADMIN':
        return Response({"error": "Only Admin can create users"}, status=403)
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_list(request):
    if request.user.role != 'ADMIN':
        return Response({"error": "Only Admin can view users"}, status=403)

    users = CustomUser.objects.all().values('id', 'username', 'email', 'role')
    return Response(list(users))
