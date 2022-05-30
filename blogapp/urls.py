from django.urls import path
from .views import (
    ArticleListView,
)

from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('articles-list', ArticleListView.as_view(), name='articles_list'),
    # path('article-detail/<int:pk>',ArticlesDetailView.as_view(), name='article_detail'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    

]

"""
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk4NTE0OCwiaWF0IjoxNjUzODk4NzQ4LCJqdGkiOiI5MmZmNzQ1YTdiZTk0ZWQ5ODU0YWY0OTJhOTA0NmYyMiIsInVzZXJfaWQiOjF9.eoAL3WTw1ERUawFn3yVosIQPtd79Al_BjMhqHmmR_qk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzODk5MDQ4LCJpYXQiOjE2NTM4OTg3NDgsImp0aSI6ImQ1ZDlkNjhkMWIzODQ1OGQ4ZjY4ZDllMjE3OWQ2OTdjIiwidXNlcl9pZCI6MX0.qICkTradQHhUsqBy8iu7AWce9Kfw12RtIRbyuhLlqGM"
}
"""