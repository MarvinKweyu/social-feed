from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Action(models.Model):
    """Record user interactions within the system"""
    user = models.ForeignKey(
        'auth.User', related_name='actions', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=200)
    # do not record yourself while saving .i.e blank=True
    target_ct = models.ForeignKey(
        ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(
        blank=True, null=True, db_index=True)

    target = GenericForeignKey('target_ct', 'target_id')
    # use time the object was created
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        # latest actions first
        ordering = ('-created',)
