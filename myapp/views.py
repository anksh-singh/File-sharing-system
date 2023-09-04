from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import FileSystemStorage
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import OpsCliUsers, UploadFile
from .serializers import CustomUserSerializer, FileSerializer
from django.http import JsonResponse, Http404
from Utility import constants as const
import json
from myapp import models

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from helper_func import get_activation_link


# Sign up API
@api_view(['POST'])
def signup_view(request):
    response = {}
    data = json.loads(request.body)
    if data.get('email', None) and data.get('password', None) and data.get('user_type', None):
        user_exist = models.OpsCliUsers.objects.filter(email=data.get('email')).first()
        if not user_exist:
            user = models.OpsCliUsers.objects.create(
                email=data.get('email'),
                name=data.get('name', ''),
                user_type = data.get('user_type'),
                password=make_password(data.get('password')),
            )
            # triggering a emaill notification for verification
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Mail objects
            site_link = get_activation_link(user)
            mail_subject = 'Activate your FileSync account.'
            message = f'''
            Hello {user.name},
            Please click on the link below to activate your account:
            {site_link}

            Thank you,
            '''
            send_mail(
                mail_subject,
                message,
                'noreply0110@gmail.com', 
                [user.email], 
                fail_silently=False,
            )
     
            response['statusCode'] = const.SUCCESS_STATUS_CODE
            response['message'] = 'Signed up successfully!'
              
        else:
            response['statusCode'] = const.ALREADY_EXIST_ERROR_CODE
            response['message'] = 'You have already registered. Please try to login!'
   
    return JsonResponse(response)


# Login API
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
                'message' : f"User logged as {user.user_typ} successfully!"
            }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'message': const.USER_NOT_FOUND}, status=const.NOT_AUTHORIZED_ERROR_CODE)  
    
    
    
# Upload Files API
@api_view(['POST'])
def FileUploadView(request):
        user = request.user
        if user.user_type == "CLIENT":
            return Response({'error': 'Not an Operational User'}, status=status.HTTP_403_FORBIDDEN)

        uploaded_file = request.FILES.get('file')
        
        if not (uploaded_file.name.endswith('.pptx') or uploaded_file.name.endswith('.docx') or uploaded_file.name.endswith('.xlsx')):
            return Response({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

        if uploaded_file is None:
            return Response({'error': 'No file uploaded'}, status=const.NOT_FOUND)

        fs_obj = FileSystemStorage()
        filename = fs_obj.save(uploaded_file.name, uploaded_file)
        file_url = fs_obj.url(filename)
        
        return Response({'file_url': file_url}, status=const.SUCCESS_STATUS_CODE)
    
    


    
    
