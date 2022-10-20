from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, PostSerializer, CommentSerializer

from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет группы"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет поста"""
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментария"""
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_update(self, serializer):
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        instance.delete()
