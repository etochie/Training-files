from django.urls import path
from rest_framework import routers

from .views import ArticleView

router = routers.DefaultRouter()
router.register(r'articles', ArticleView, basename='user')
urlpatterns = router.urls
# urlpatterns = [
#     path('articles/', ArticleView.as_view())
# ]

