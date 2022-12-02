from django.contrib import admin

from stake.models import Chain, Stake


# Register your models here.


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ["name", "symbol", "logo"]
    list_editable = ["symbol"]
    ordering = ["name"]
    search_fields = ["name", "symbol"]


@admin.register(Stake)
class StakeAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ["asset_image", "asset_to_stake", "asset_to_win", "apy", "chain"]
    list_display_links = ["asset_to_stake"]
    list_select_related = ["chain"]
    ordering = ["asset_to_stake", "asset_to_win"]
    readonly_fields = ["slug"]
    search_fields = ["asset_to_stake", "asset_to_win"]
