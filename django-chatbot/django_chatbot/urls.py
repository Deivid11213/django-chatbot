from django.contrib import admin
from django.urls import path, include
import chatbot.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(chatbot.urls)),
]