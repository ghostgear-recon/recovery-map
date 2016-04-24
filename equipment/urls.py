from django.conf.urls import url
from .views import ListEquipmentAPIView

urlpatterns = [
    url(r'list$',   csrf_exempt(ListEquipmentView.as_view())),
]
