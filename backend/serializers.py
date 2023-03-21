from rest_framework import serializers

from .models import *

class User_create_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
class Renobe_Serializer(serializers.ModelSerializer):
    tags=serializers.StringRelatedField(many=True)
    writer_user_id=serializers.StringRelatedField()
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