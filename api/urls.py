from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import GymViewSet, TrainerViewSet, ClientViewSet, WorkoutSessionViewSet

router = DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gym')
router.register(r'trainers', TrainerViewSet, basename='trainer')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'workoutsessions', WorkoutSessionViewSet, basename='workoutsession')

urlpatterns = [
    path('', include(router.urls)),
]