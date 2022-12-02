from rest_framework import serializers

from stake.models import Chain, Stake


# Create your serializers


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = ("id", "slug", "name", "symbol", "logo", "created")


class StakeSerializer(serializers.ModelSerializer):
    chain = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Chain.objects.all())

    class Meta:
        model = Stake
        fields = ("id", "slug", "asset_to_stake", "asset_image", "asset_to_win", "apy", "chain", "contract_address", "created")
