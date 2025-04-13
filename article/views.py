from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Comment
from .serializer import ArticelSerializer, CommentSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import UserPermission, IsOwnerOrReadOnly
from datetime import date
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions,renderers

class ShowArticle(APIView):
    permission_classes = [IsAuthenticated, UserPermission]

    def get(self, request):
        instance = Article.objects.all()
        ser = ArticelSerializer(instance=instance, many=True)
        return Response(ser.data)


class AddArticle(APIView):
    permission_classes = [UserPermission, IsOwnerOrReadOnly]

    def post(self, request):
        data = request.data.copy()
        # data['user'] = request.user.id
        data['date'] = date.today()
        ser = ArticelSerializer(data=data)
        if ser.is_valid():
            ser.validated_data['user'] = request.user
            ser.save()
            return Response({'massage': 'article add'})
        return Response(ser.errors)


class AddComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        comment_data = request.data.copy()
        comment_data['article'] = pk
        comment_data['owner'] = request.user.id
        ser = CommentSerializer(data=comment_data)
        print(request.user)
        if ser.is_valid():
            ser.save()
            return Response({'massage': 'comment add'})
        return Response(ser.errors)


class DeleteArticle(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        intance = Article.objects.get(id=pk)
        intance.delete()
        return Response({'massage': 'article is delete'})


class DeleteComment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        instance = Comment.objects.get(id=pk)
        instance.delete()
        return Response({'massage': 'comment is delete'})


class CheckUser(APIView):

    def get(self, request):
        user = request.user
        return Response({'user': user.username})


class UpdateArticle(APIView):
    permission_classes = [IsOwnerOrReadOnly, UserPermission]

    def post(self, request, pk):
        instance = Article.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        ser = ArticelSerializer(instance=instance, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'massage': 'article is update'})
        return Response({'massage': 'failed'})


class UpdateComment(APIView):
    permission_classes = [IsOwnerOrReadOnly, UserPermission]

    def post(self, request, pk):
        instance = Comment.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        ser = CommentSerializer(instance=instance, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'massage': 'comment is update'})
        return Response({'massage': 'failed'})


class UserDetail(APIView):
    def get(self, request):
        user = User.objects.all()
        ser = UserSerializer(instance=user, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class ArticelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticelSerializer

    def perform(self,serializer):
        serializer.save(owner=self.request.user)


class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform(self,serializer):
        serializer.save(owner=self.request.user)