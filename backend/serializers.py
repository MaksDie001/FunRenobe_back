from rest_framework import serializers

from .models import *

class Renobe_img_add_Serializers(serializers.ModelSerializer):
    writer_user_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Renobe
        fields=("renobe_img","writer_user_id","autor_check")

class Tags_serializers(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields=["id","tags"]
class Renobe_Serializer(serializers.ModelSerializer):
    tags=serializers.StringRelatedField(many=True)
    writer_user_id=serializers.StringRelatedField()
    total_likes=serializers.SerializerMethodField()
    total_dislikes=serializers.SerializerMethodField()
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

class Renobe_chapters_list_serializers(serializers.ModelSerializer):
    class Meta:
        model=Renobe_chapters
        fields="__all__"

class Country_serializers(serializers.ModelSerializer):
    class Meta:
        model=Counrty
        fields="__all__"