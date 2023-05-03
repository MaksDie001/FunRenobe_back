from django.contrib.auth import get_user_model


import requests
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    avatar_img = models.ImageField(upload_to="photos/%Y/%m/%d/")
    last_join = models.DateTimeField(auto_now_add=True,null=True,auto_created=True)
    is_writer = models.BooleanField(default=False,null=True)
    phone = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.username

class Counrty(models.Model):
    country_name=models.CharField(max_length=155)
    country_banner=models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.country_name
class Translation_status(models.Model):
    translation_status = models.CharField(max_length=155)

    def __str__(self):
        return self.translation_status

class Renobe_status(models.Model):
    renobe_status=models.CharField(max_length=155)

    def __str__(self):
        return self.renobe_status

class Renobe_chapters(models.Model):
    chapter_title = models.CharField(max_length=155)
    chapter_text=models.TextField()
    translators = models.ManyToManyField(User, related_name="transletor")
    date_time=models.DateTimeField(auto_created=True,auto_now_add=True,null=True)
    audio = models.FileField(upload_to="audio/%Y/%m/%d/")
    chapter_number = models.IntegerField(default=0)
    renobe=models.ForeignKey("Renobe",related_name="Renobe",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.chapter_title

    class Meta:
        ordering = ["-date_time"]


class Renobe(models.Model):
    renobe_status_choices=(
        ("выпускается","выпускаеется"),
        ("работа приостановлена","работа приостановлена"),
        ("Заброшенна","Заброшенна")
    )
    translation_status_choices=(
        ("перевод идет","перевод идет"),
        ("перевод приостановлен","перевод приостановлен"),
        ("Заброшенна","Заброшенна")
    )
    slug=models.SlugField()
    writer_user_id = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name="writer")
    renobe_name = models.CharField(max_length=255,unique=True)
    renobe_title = models.TextField()
    renobe_img=models.ImageField(upload_to="photos/%Y/%m/%d/",null=True)
    date_join = models.DateField(auto_created=True,auto_now_add=True)
    last_update = models.DateTimeField(auto_created=True, auto_now_add=True)
    tags = models.ManyToManyField("Tags")
    country=models.ForeignKey(Counrty,on_delete=models.SET_DEFAULT,default="нейзвестно")
    renobe_status=models.CharField(max_length=155,choices=renobe_status_choices)
    transnlation_status=models.CharField(max_length=155,choices=translation_status_choices)
    Note=models.CharField(max_length=255,default="отсутствует ")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    def total_likes(self):
        return self.likes.count()
    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.renobe_name




class Group(models.Model):
    name = models.CharField(max_length=155)
    group_admin = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="group_admin",null=True)
    group_members = models.ManyToManyField(User, related_name="group_members")
    title = models.TextField()
    group_tematic = models.TextField()
    group_tematic_tags = models.ManyToManyField("Tags")
    date_join = models.DateField(auto_created=True)


class Tags(models.Model):
    tags = models.CharField(max_length=55,unique=True)
    description_short = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.tags

class Comment(models.Model):
    text = models.TextField
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    self = models.ForeignKey("Comment", on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post = models.ForeignKey(Renobe, on_delete=models.SET_NULL,null=True)


class Team_group(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)

