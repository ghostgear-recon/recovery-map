import logging
logger = logging.getLogger(__name__)

from PIL import ExifTags, Image

from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic.base import View

from .models import Equipment
from .utils import get_lat_lon


class CreateEquipmentView(View):

    def post(self, request, *args, **kwargs):
        if len(request.FILES) != 1:
            logger.error('Only one file allowed')
            raise Http404

        input_image = request.FILES['file']
        image = Image.open(input_image)
        exif = dict((ExifTags.TAGS[k], v) for k, v in image._getexif().items() if k in ExifTags.TAGS)
        if 'GPSInfo' not in exif:
            logger.error('No GPSInfo in image exif data')
            raise Http404

        gps_exif = dict((ExifTags.GPSTAGS[k], v) for k, v in exif['GPSInfo'].items() if k in ExifTags.GPSTAGS)
        latitude, longitude = get_lat_lon(gps_exif)

        equipment = Equipment.objects.create(latitude=latitude, longitude=longitude, image=input_image)

        max_dimension, width, height = 512, equipment.image.width, equipment.image.height
        ratio = min(float(max_dimension)/width, float(max_dimension)/height)
        if ratio < 1:
            equipment.image = image.resize((int(ratio*width), int(ratio*height)), Image.ANTIALIAS)
            equipment.save()

        return HttpResponse()


class ListEquipmentView(View):

    def get(self, request, *args, **kwargs):
        equipment = Equipment.objects.all()
        return JsonResponse({
            'equipment':
            [
                {
                    'latitude':e.latitude,
                    'longitude': e.longitude,
                    'retrieved': e.retrieved,
                    'uuid': e.uuid,
                    'image': e.image.url,
                    'created': e.created,
                } for e in equipment
            ]
        })
