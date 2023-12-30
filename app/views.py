from rest_framework import viewsets, status
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Gym, Trainer, Client, WorkoutSession
from .serializers import GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer
from .auth import IsTrainerOrReadOnly


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    
    # Handle invalid input data
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    # check if the user is a trainer(admin) or a client
    permission_classes = [IsTrainerOrReadOnly]

