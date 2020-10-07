from django.urls import path, include
from . import views
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
from rest_framework import routers
from .api import TaskViewSet


router = routers.DefaultRouter()
router.register('api/task', TaskViewSet, 'task')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', views.apiOverview, name='api-overview'),
    path('api/task-list/', views.taskList, name='task-list'),
    path('api/task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('api/task-create/', views.taskCreate, name='task-update'),
    path('api/task-update/<str:pk>/', views.taskUpdate, name='task-create'),
    path('api/task-delete/<str:pk>/', views.taskDelete, name='task-delete'),

    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]
