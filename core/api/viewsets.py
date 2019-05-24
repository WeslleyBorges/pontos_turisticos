from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    lookup_field = 'nome'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):

        nome = self.request.query_params.get('nome', None)

        cutesat = PontoTuristico.objects.all()

        if nome:
            cutesat = cutesat.filter(nome__contains=nome)

        return cutesat

    def list(self, request, *args, **kwargs):
        #return Response({'modelo': 'Corsa', 'ano': 2006, 'flex': True})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        ponto_turistico = PontoTuristico.objects.get(pk=kwargs['pk'])
        ponto_turistico.descricao = request.data['descricao']

        ponto_turistico.save()

        return Response({'mensagem': 'O objeto foi atualizado com sucesso.'})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)