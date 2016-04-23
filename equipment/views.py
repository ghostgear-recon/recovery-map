import logging
logger = logging.getLogger(__name__)

from django.views.generic.base import View
from django.http import JsonResponse

from .models import Equipment


class ListEquipmentAPIView(View):

    def get(self, request, *args, **kwargs):
        equipment = Equipment.objects.all()
        logger.warn('dump')
        logger.warn(equipment)
        return JsonResponse({
            'equipment':
            [
                {
                    'latitude':e.latitude,
                    'longitude': e.longitude,
                    'retrieved': e.retrieved,
                    'uuid': e.uuid
                } for e in equipment
            ]
        })
