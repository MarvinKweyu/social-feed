from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from images.models import Image


@receiver(m2m_changed, sender=Image.user_like.through)
def user_like_changed(sender, instance, **kwargs):
    # BUG: unable to update the total_likes counter or this entire field

    print(f"\n saving the object {instance.total_likes}")
    instance.total_likes = instance.user_like.count()
    print("*" * 25)
    print(f"Observe the likes change object: {instance.total_likes}")
    print("*" * 25)
    instance.save()
    print("total likes..")
    print(instance.total_likes)
