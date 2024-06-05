from django.contrib import admin
from django.urls import path

from polls.views import word_list,lobby,termo


urlpatterns =[
    path('admin/', admin.site.urls),
    path("", lobby, name="lobby"),
    path("palavras/", word_list, name="word_list"),
    path("jogo/", termo, name="termo"),
]

