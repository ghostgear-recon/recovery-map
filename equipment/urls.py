from django.conf.urls import url
from .views import ListEquipmentAPIView

urlpatterns = [
    url(r'list', ListEquipmentAPIView.as_view())
]
