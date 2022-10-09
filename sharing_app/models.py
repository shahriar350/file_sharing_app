from django.db import models


# Create your models here.
class FileLink(models.Model):
    link = models.URLField()


class ShareFile(models.Model):
    file = models.FileField()
    link = models.ForeignKey(FileLink, on_delete=models.CASCADE, related_name="get_files")
