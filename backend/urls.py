from django.urls import path
from .views import *

urlpatterns = [
    path("", Renobe_chapters_API.as_view()),
    path("Renobe/img/add/<slug:slug>",Renobe_img_add_API.as_view()),
    path("user_show", User_show.as_view()),
    path("country", Country_show_API.as_view()),
    path("country/<int:pk>", Country_one_show_API.as_view()),
    path("chapter/<str:pk>", Renobe_chapters_List.as_view()),
    path("renobe/<slug:slug>", One_Renobe_API.as_view()),
    path("renobe/add/", One_renobe_add_API.as_view()),
    path("tags_list",Tags_API.as_view()),
    path("<int:pk>", One_Renobe_API.as_view()),
    path('<int:pk>/like/', AddLike.as_view()),
    path('<int:pk>/dislike/', AddDislike.as_view()),
    path("user/<int:pk>",User_profile.as_view()),
    path("user_renobe",User_renobe.as_view()),
    path("renobe/chapters_add/<int:pk>",Renobe_chapter_add.as_view()),
    path("last_chapter/<int:pk>",Renobe_last_chapter.as_view()),
    path("hz",hz.as_view())
]
