from rest_framework import viewsets, filters, generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Post, Comment, Like, Notification
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


# -----------------------
# Pagination
# -----------------------
class PostPagination(PageNumberPagination):
    page_size = 5


# -----------------------
# Feed
# -----------------------
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    paginator = PostPagination()
    paginated_posts = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(paginated_posts, many=True)
    return paginator.get_paginated_response(serializer.data)


# -----------------------
# Likes
# -----------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    """
    Like a post. Prevents duplicate likes and creates a notification.
    """
    post = generics.get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"message": "You already liked this post"}, status=400)

    if post.author != request.user:
        Notification.objects.create(
            user=post.author,
            sender=request.user,
            action='like',
            target=post
        )

    return Response({"message": "Post liked successfully"}, status=201)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    """
    Unlike a post if the user has previously liked it.
    """
    post = generics.get_object_or_404(Post, pk=pk)

    deleted, _ = Like.objects.filter(user=request.user, post=post).delete()
    if deleted == 0:
        return Response({"error": "Like not found"}, status=404)

    return Response({"message": "Post unliked successfully"}, status=200)


# -----------------------
# ViewSets
# -----------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)