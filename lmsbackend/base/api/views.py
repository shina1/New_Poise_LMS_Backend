from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny


class CustomUserCreate(APIView):
    permissions_classes = [AllowAny]


    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                status_code = status.HTTP_201_CREATED
                response={
                    'success': True,
                    'statusCode' : status_code,
                    'message' : 'User successfully registered!',
                    'user': reg_serializer.data
                }
                return Response(response, status_code)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)