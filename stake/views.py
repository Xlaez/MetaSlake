from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from stake.models import Chain, Stake
from stake.serializers import ChainSerializer, StakeSerializer


# Create your views here.


class ChainView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StakeView(ListCreateAPIView):
    queryset = Stake.objects.select_related("chain").all()
    serializer_class = StakeSerializer


class StakeUpdateView(RetrieveUpdateAPIView):
    queryset = Stake.objects.select_related("chain").all()
    serializer_class = StakeSerializer
    lookup_field = "slug"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {"asset_to_stake": request.data.get("asset_to_stake"), "asset_image": request.data.get("asset_image"),
                "asset_to_win": request.data.get("asset_to_win"), "apy": request.data.get("apy"),
                "chain": request.data.get("chain"), "contract_address": request.data.get("contract_address")}
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
