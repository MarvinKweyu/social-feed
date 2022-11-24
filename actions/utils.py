import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from actions.models import Action

"""
Record the following metrics within the platform
- A user bookmarks an image
• A user likes an image
• A user creates an account
• A user starts following another user

"""


def create_action(user, verb, target=None):
    """Record an action performed by a user"""

    # * Note:
    # timezone.now() similar to datetime.now() but returns a timezone aware object

    last_minute = timezone.now() - datetime.timedelta(seconds=60)
    # get all actions swithin the last minute
    similar_actions = Action.objects.filter(
        user_id=user.id, verb=verb, created__gte=last_minute)

    if not similar_actions:
        # no similar actions recorded
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
            target_ct=target_ct, target=target.id)
    return False
