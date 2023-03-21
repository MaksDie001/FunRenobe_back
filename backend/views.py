from django.views.generic import *
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpRequest, HttpResponseRedirect, HttpResponse


class User_API(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class=User_create_serializer
class User_create_API(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class=User_create_serializer
class One_Renobe_API(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Renobe.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = Renobe_Serializer

class Renobe_chapters_List(generics.ListAPIView):
    serializer_class = Renobe_chapters_list_serializers

    def get_queryset(self):
        x=self.kwargs["pk"]
        return Renobe_chapters.objects.filter(renobe__slug=x)

class Renobe_chapters_API(generics.ListAPIView):
    queryset = Renobe_chapters.objects.all()
    serializer_class = Renobe_chapters_serializers
class Country_API(generics.RetrieveAPIView):
    queryset = Counrty.objects.all()
    serializer_class=Country_serializers


class AddLike(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        try:
            post = Renobe.objects.get(pk=pk)
        except Renobe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        return Response(status=status.HTTP_200_OK)



class AddDislike(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        try:
            post = Renobe.objects.get(pk=pk)
        except Renobe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        return Response(status=status.HTTP_200_OK)