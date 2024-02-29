from django.urls import path
from .views import RegisterView, RetrieveUserView, UserBuyView, ItemsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view()),
    path('userbuy', UserBuyView.as_view()),
    path('items', ItemsView.as_view()),
]