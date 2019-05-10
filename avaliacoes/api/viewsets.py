from rest_framework.viewsets import ViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer