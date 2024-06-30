
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Chauffeur
from .serializers import ChauffeurSerializer
from utilisateurs.permissions import IsAdminOrIsManager

class ChauffeurViewSet(viewsets.ModelViewSet):
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurSerializer
    permission_classes = [IsAuthenticated, IsAdminOrIsManager]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
