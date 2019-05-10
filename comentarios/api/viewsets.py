from rest_framework.viewsets import ViewSet
from .serializers import ComentarioSerializer
from comentarios.models import Comentario

class ComentarioViewSet(ViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer