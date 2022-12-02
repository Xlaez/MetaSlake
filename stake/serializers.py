from rest_framework import serializers

from stake.models import Stake


# Create your serializers


class StakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stake
        fields = ("id", "asset_to_stake", "asset_image", "asset_to_win", "apy", "contract_address", "created")
