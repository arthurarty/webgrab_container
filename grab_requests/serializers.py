from grab_requests.models import GrabRequest
from rest_framework import serializers
from typing import Dict, Any
from common.custom_logging import logger
from grab_requests.tasks import run_web_grab


class GrabRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabRequest
        fields = [
            'id',
            'site', 
            'site_id',
            'xmltv_id',
            'result_xml', 
            'status',
            'result_log',
            'channel_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'result_xml',
            'id',
            'status',
            'result_log',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data: Dict[str, Any]) -> GrabRequest:
        grab_request = GrabRequest.objects.create(**validated_data)
        run_web_grab.delay(
            grab_request.id, grab_request.site, grab_request.site_id, grab_request.xmltv_id, grab_request.channel_name
        )
        return grab_request
