from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import OpsCliUsers, UploadFile
from .serializers import CustomUserSerializer, FileSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        # Issue token and return
        pass
    else:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_file(request):
    pass
    # Check if user is Ops User and handle file upload

# @api_view(['POST'])
# def signup_view(request):
#     pass
    # Signup logic with encrypted URL

# ... Implement other endpoints