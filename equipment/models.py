from __future__ import unicode_literals

import uuid
from django.db import models


class Equipment(models.Model):

    class Meta:
        ordering = ('-created', )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    image = models.ImageField(upload_to='equipment')
    contact_number = models.TextField(max_length=15, null=True)
    retrieved = models.BooleanField(default=False)

    def __unicode__(self):
        return '{} ({}, {})'.format(self.uuid, self.latitude, self.longitude)
