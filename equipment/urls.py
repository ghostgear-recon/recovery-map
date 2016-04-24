from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import CreateEquipmentView, ListEquipmentView

urlpatterns = [
    url(r'create/?$', csrf_exempt(CreateEquipmentView.as_view())),
    url(r'list/?$',   csrf_exempt(ListEquipmentView.as_view())),
]
