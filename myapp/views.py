from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.core.files.storage import FileSystemStorage
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import OpsCliUsers, UploadFile
from .serializers import CustomUserSerializer, FileSerializer
from django.http import JsonResponse
from Utility import constants as const

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        data = {
                'token': token.key,
                'user_type' : user.user_type,   # based on the user id front-end can understand which dashboard to show for operation/client user
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'message' : "User logged in successfully!" 
            }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'message': const.USER_NOT_FOUND}, status=const.NOT_AUTHORIZED_ERROR_CODE)  
    
    
    
    
@api_view(['POST'])
class FileUploadView(APIView):
    def post(self, request):
        user = request.user
        if user.user_type == "OPS":
            return Response({'error': 'Not an Operational User'}, status=status.HTTP_403_FORBIDDEN)

        uploaded_file = request.FILES.get('file')

        if uploaded_file is None:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        if not (uploaded_file.name.endswith('.pptx') or uploaded_file.name.endswith('.docx') or uploaded_file.name.endswith('.xlsx')):
            return Response({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        return Response({'file_url': file_url}, status=const.SUCCESS_STATUS_CODE)