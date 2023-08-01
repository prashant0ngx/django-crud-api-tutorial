from sqlite3 import IntegrityError
from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, LoginSerializer
from .filters import UserFilter
from .decorators import filter_class
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from django.conf import settings

# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny,])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
        LoginSerializer().validate(request.data)
           # also send is_staff and is_superuser
        user = User.objects.get(username=username, password=password) 
        if user:
            try:
                payload = RefreshToken.for_user(user)
                token = str(payload.access_token)
                user_details = {}
                user_details['username'] = "%s" % (
                    user.username)
                user_details['token'] = token
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                res = {'error': 'Can not generate token' + str(e) }
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        else:
            res = {
                'error': 'Can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'Please provide a username and a password'}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    try:
        UserSerializer().validate(request.data)
        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password'],
            
        )
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

            

@api_view(['POST'])
@authentication_classes([TokenAuthentication, ])
def create_user(request):
    try:
        
        UserSerializer().validate(request.data)
        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password'],
            is_staff=request.data['is_staff'].lower() == 'true',
        )
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['GET'])
@permission_classes([AllowAny, ])
@filter_class(UserFilter)
def get_all_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([AllowAny, ])
@filter_class(UserFilter)
def get_user_by_id(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])
@permission_classes([AllowAny, ])
@filter_class(UserFilter)
def update_user_by_id(request, pk):
    try:
        UserSerializer().validateUpdate(request.data)
        user_update = User.objects.filter(pk=pk).update(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        
        return Response(status=status.HTTP_200_OK)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@filter_class(UserFilter)
def delete_user_by_id(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


        





# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_class = UserFilter
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save()
    
#     def get_queryset(self):
#         return User.objects.all().order_by('-id')
    





# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_class = UserFilter
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save()
    
#     def get_queryset(self):
#         return User.objects.all().order_by('-id')
    
#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
#         return obj
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    

    







