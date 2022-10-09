import uuid

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

my_user = get_user_model()


# Create your models here.
class FileLink(models.Model):
    link = models.UUIDField(default=uuid.uuid4)

    # user = models.ForeignKey(my_user, on_delete=models.CASCADE, related_name="get_user_links", null=True, blank=True)

    def __str__(self):
        return str(self.link)


class ShareFile(models.Model):
    file = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpeg", "jpg", "png", "zip"],
                                           message='Only "pdf", "jpeg", "jpg", "png", "zip" are acceptable.')]
    )
    link = models.ForeignKey(FileLink, on_delete=models.CASCADE, related_name="get_files", blank=True)
