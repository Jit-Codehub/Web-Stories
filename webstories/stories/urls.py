from django.urls import path,include
from stories import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home',views.homepage),
    path('web-stories/<str:story>/',views.webstories)
] 