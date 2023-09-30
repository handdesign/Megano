import json

from django.contrib.auth import authenticate, update_session_auth_hash, logout, login
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import User, Profile
from .serializers import ProfileSerializer, SignInSerializer, SignUpSerializer, ChangePasswordSerializer


@api_view(['POST'])
def sign_in(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = SignInSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User.objects.create_user(username=username, password=password)

            user.first_name = name
            user.save()

            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def profile_detail(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        old_password = serializer.data.get('old_password')
        new_password = serializer.data.get('new_password')

        if request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()

            update_session_auth_hash(request, request.user)

            return Response({'message': 'Password changed successfully'})
        else:
            return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_avatar(request):
    user = request.user

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if 'avatar' in request.FILES:
        profile.avatar = request.FILES['avatar']
        profile.save()
        return Response({'message': 'Avatar changed successfully'})
    else:
        return Response({'error': 'No avatar uploaded'}, status=status.HTTP_400_BAD_REQUEST)
