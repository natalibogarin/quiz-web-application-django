from django.contrib import admin
from .models import *

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Avg
from django.db.models.functions import TruncDay

# Register your models here.

@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display=('question', 'ans')
    search_fields=('question',)
    list_per_page=25

@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display=('time', 'score', 'reg_date', 'correct', 'wrong', 'percent')
    search_fields=('reg_date',)
    list_per_page=25

    def changelist_view(self, request, extra_context=None):
        
        GData = (
            GameModel.objects.annotate(date=TruncDay("reg_date"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        PData = (
            GameModel.objects.values("id")
            .annotate(date=TruncDay("reg_date"))
            .values("date")
            .annotate(y=Avg("score"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        game_as_json = json.dumps(list(GData), cls=DjangoJSONEncoder)
        points_as_json = json.dumps(list(PData), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"GData": game_as_json, "PData": points_as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(UserVisit)
class UserVisitAdmin(admin.ModelAdmin):

    list_display = ("timestamp", "user", "session_key", "remote_addr")
    list_filter = ("timestamp",)
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__username",
        "ua_string",
    )
    raw_id_fields = ("user",)
    readonly_fields = (
        "user",
        "hash",
        "timestamp",
        "session_key",
        "remote_addr",
        "ua_string",
        "created_at",
    )
    ordering = ("-timestamp",)
    list_per_page=25

    def changelist_view(self, request, extra_context=None):
        
        UData = (
            UserVisit.objects.annotate(date=TruncDay("timestamp"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        visits_as_json = json.dumps(list(UData), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"UData": visits_as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

