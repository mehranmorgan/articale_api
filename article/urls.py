from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'article'

urlpatterns = [
    path('show', views.ShowArticle.as_view(), name='article_show'),
    path('add_article', views.AddArticle.as_view(), name='article_add'),
    path('add_comment/<int:pk>', views.AddComment.as_view(), name='comment_add'),
    path('delete_article/<int:pk>', views.DeleteArticle.as_view(), name='article_delete'),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(), name='comment_delete'),
    path('check', views.CheckUser.as_view(), name='check_user'),
    # path('login', Token_view.obtain_auth_token, name='login'),
    path('update_article/<int:pk>', views.UpdateArticle.as_view(), name='update_article'),
    path('update_comment/<int:pk>', views.UpdateComment.as_view(), name='update_comment'),
    path('user', views.UserDetail.as_view(), name='User_Detail'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
router = DefaultRouter()
router.register(r'article/set', views.ArticelViewSet, basename='article')
router.register(r'user/set', views.UserViewset, basename='user')
router.register(r'comment/set', views.CommentsViewset, basename='comment')

urlpatterns += [
    path('', include(router.urls)),
]
