from rest_framework.viewsets import ModelViewSet
from .serializers import AtracaoSerializer
from atracoes.models import Atracao
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    permission_classes = (IsAdminUser, )

    filter_backends = (filters.SearchFilter, )
    search_fields = ('nome',)
    filter_fields = ('nome',)
