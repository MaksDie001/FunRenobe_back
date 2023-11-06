from rest_framework import serializers

from .models import *

class Renobe_img_add_Serializers(serializers.ModelSerializer):
    writer_user_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Renobe
        fields=("renobe_img","writer_user_id")

'''class User_Bookmarks_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=("bookmarks",)'''



class Tags_serializers(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields=["id","tags"]

class Renobe_Serializer(serializers.ModelSerializer):
    tags=serializers.StringRelatedField(many=True)
    writer_user_id=serializers.StringRelatedField()
    total_likes=serializers.SerializerMethodField()
    total_dislikes=serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    disliked = serializers.SerializerMethodField()

    def get_liked(self, obj):
        request = self.context.get('request')
        return obj.likes.filter(id=request.user.id).exists()

    def get_disliked(self, obj):
        request = self.context.get('request')
        return obj.dislikes.filter(id=request.user.id).exists()

    def get_total_dislikes(self,obj):
        return obj.total_dislikes()
    def get_total_likes(self,obj):
        return obj.total_likes()
    class Meta:
        model = Renobe
        fields = "__all__"



class Renobe_add_serializers(serializers.ModelSerializer):
    class Meta:
        model = Renobe
        fields = "__all__"

class Renobe_chapters_serializers(serializers.ModelSerializer):
    renobe=Renobe_Serializer()
    class Meta:
        model=Renobe_chapters
        fields="__all__"

class Renobe_Serializer_writer_id(serializers.ModelSerializer):
    writer_user_id = serializers.StringRelatedField()

    class Meta:
        model = Renobe
        fields = ("writer_user_id",)
class Renobe_chapters_serializers_add(serializers.ModelSerializer):
    class Meta:
        model=Renobe_chapters
        fields="__all__"


class Renobe_chapters_list_serializers(serializers.ModelSerializer):
    class Meta:
        model=Renobe_chapters
        fields="__all__"

class Country_serializers(serializers.ModelSerializer):
    class Meta:
        model=Counrty
        fields="__all__"

class User_serializers(serializers.ModelSerializer):
    bookmarks = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=User
        fields="__all__"

class Int_ser(serializers.Serializer):
    chapter_number=serializers.IntegerField()