from django.contrib import admin
from django.urls import path
from app.views import hello_view, home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("<name>/", hello_view),
]
