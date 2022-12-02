from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from stake.models import Chain, Stake
from stake.serializers import StakeSerializer


# Create your views here.


class ChainView(APIView):
    def get(self, request):
        chains = Chain.objects.values("id", "name", "symbol", "logo", "created")
        return Response(chains, status=200)


class StakeView(ListCreateAPIView):
    queryset = Stake.objects.select_related("chain").all()
    serializer_class = StakeSerializer
