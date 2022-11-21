from django.db import models
from django.conf import settings


class Profile(models.Model):
    """User profile"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


class Contact(models.Model):
    """Hold relationship for follower accounts"""
    user_to = models.ForeignKey('auth.User', related_name="rel_from_set" on_delete=models.CASCADE)
    user_from = models.ForeignKey(
        'auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    # improve queries ordering results by this field
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return f"{self.user_from} follows {self.user_to}"
