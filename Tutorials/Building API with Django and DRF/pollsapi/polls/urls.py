from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import PollList, PollDetail
from .views import PollsViewSet
from .views import ChoiceList
from .views import CreateVote
from .views import UserCreate


router = DefaultRouter()
router.register('polls', PollsViewSet, basename='polls')


urlpatterns = [
    # path('polls/',PollList.as_view(), name='polls_list'),
    # path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('signin/', UserCreate.as_view(), name='user_create')
]

urlpatterns += router.urls
