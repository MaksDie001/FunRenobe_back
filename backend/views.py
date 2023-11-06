from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
class hz(generics.ListAPIView):
    serializer_class = Renobe_chapters_serializers_add
    queryset = Renobe_chapters.objects.all()
class Renobe_chapter_add(generics.CreateAPIView):
    serializer_class = Renobe_chapters_serializers_add
    queryset = Renobe_chapters.objects.all()
    def post(self, request, *args, **kwargs):
        writer_user_id=Renobe.objects.get(id=kwargs['pk']).writer_user_id
        if str(writer_user_id) == str(request.user.username):
            request.data['renobe'] = kwargs['pk']
            return self.create(request, *args, **kwargs)
        else:
            print("blya")
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class User_renobe(generics.ListAPIView):
    serializer_class =Renobe_Serializer
    lookup_field = "slug"
    def get_queryset(self):
        return Renobe.objects.filter(writer_user_id=self.request.user.id)

class User_profile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializers
    permission_classes = [IsAuthenticated,]


class Renobe_img_add_API(generics.RetrieveUpdateAPIView):
    queryset = Renobe.objects.all()
    serializer_class = Renobe_img_add_Serializers
    lookup_field = "slug"

    def put(self, request, *args, **kwargs):
        data = super().get(request, *args, **kwargs)
        if data.data["writer_user_id"] == request.user.id:
            return self.update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class One_renobe_add_API(generics.CreateAPIView):
    queryset = Renobe.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = Renobe_add_serializers

    def post(self, request, *args, **kwargs):
        request.data["writer_user_id"] =request.user.id
        return self.create(request, *args, **kwargs)


class One_Renobe_API(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Renobe.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = Renobe_Serializer


class Tags_API(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = Tags_serializers


class Country_show_API(generics.ListAPIView):
    serializer_class = Country_serializers
    queryset = Counrty.objects.all()


class Country_one_show_API(generics.RetrieveAPIView):
    serializer_class = Country_serializers
    queryset = Counrty.objects.all()


class Renobe_chapters_List(generics.ListAPIView):
    serializer_class = Renobe_chapters_list_serializers

    def get_queryset(self):
        return Renobe_chapters.objects.filter(renobe__slug=self.kwargs["pk"])



class Renobe_last_chapter(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request,*args, **kwargs):
        x =self.kwargs['pk']
        return Response({"chapter_number": Renobe_chapters.objects.filter(renobe=x).order_by("-chapter_number")[0].chapter_number})

class Renobe_chapters_API(generics.ListAPIView):
    queryset = Renobe_chapters.objects.all()
    serializer_class = Renobe_chapters_serializers

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

class User_show(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Response({"user_id": request.user.pk})


class AddDislike(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk, format=None):
        try:
            post = Renobe.objects.get(pk=pk)
        except Renobe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        like_exists = post.likes.filter(id=request.user.id).exists()
        if like_exists:
            post.likes.remove(request.user)

        dislike_exists = post.dislikes.filter(id=request.user.id).exists()
        if not dislike_exists:
            post.dislikes.add(request.user)
        else:
            post.dislikes.remove(request.user)

        return Response(status=status.HTTP_200_OK)
