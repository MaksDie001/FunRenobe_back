from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class Renobe_img_add_API(generics.RetrieveUpdateAPIView):
    queryset =Renobe.objects.all()
    serializer_class=Renobe_img_add_Serializers
    lookup_field = "slug"

    def put(self, request, *args, **kwargs):
        print(request.query_params)
        return self.update(request, *args, **kwargs)



class One_Renobe_API(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Renobe.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = Renobe_Serializer
class Tags_API(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = Tags_serializers
class One_renobe_add_API(generics.CreateAPIView):
    queryset = Renobe.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = Renobe_add_serializers

    def post(self, request, *args, **kwargs):
        request_0 = request.data.copy()
        print(request_0)
        request_0["writer_user_id"] = request.user.id
        return self.create(request, *args, **kwargs)

class Country_show_API(generics.ListAPIView):
    serializer_class = Country_serializers
    queryset = Counrty.objects.all()

class Country_one_show_API(generics.RetrieveAPIView):
    serializer_class = Country_serializers
    queryset = Counrty.objects.all()
class Renobe_chapters_List(generics.ListAPIView):
    serializer_class = Renobe_chapters_list_serializers

    def get_queryset(self):
        x=self.kwargs["pk"]
        return Renobe_chapters.objects.filter(renobe__slug=x)

class Renobe_chapters_API(generics.ListAPIView):
    queryset = Renobe_chapters.objects.all()
    serializer_class = Renobe_chapters_serializers

    def get(self, request, *args, **kwargs):
        # Получение списка объектов через родительский метод
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Добавление данных в список
        data = serializer.data
        post = Renobe.objects.get(pk=data[0]["id"])
        like_exists = post.likes.filter(id=request.user.id).exists()
        dislike_exists = post.dislikes.filter(id=request.user.id).exists()
        data[0]["renobe"]["liked"]=like_exists
        data[0]["renobe"]["disliked"] = dislike_exists
        print(data[0]["renobe"])
        return Response(data)

class AddLike(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        try:
            post = Renobe.objects.get(pk=pk)
        except Renobe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        dislike_exists = post.dislikes.filter(id=request.user.id).exists()
        if dislike_exists:
            post.dislikes.remove(request.user)

        like_exists = post.likes.filter(id=request.user.id).exists()
        if not like_exists:
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)

        return Response(status=status.HTTP_200_OK)
class User_show(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self,request):
        return Response({"user_id":request.user.pk})

class AddDislike(APIView):
    permission_classes = [IsAuthenticated,]

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