from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import user_feed
from django.urls import path

urlpatterns = [
    path('feed/', user_feed, name='user-feed'),
]

urlpatterns += router.urls

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls