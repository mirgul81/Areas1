
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .serializers import UserSerializer, AreasSerializer
from .models import Area



class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AreasView(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreasSerializer


class CreaeteAreaView(CreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreasSerializer


class GetAreaView(RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreasSerializer

class UpdateAreaView(UpdateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreasSerializer


class DeleteAreaView(DestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreasSerializer

