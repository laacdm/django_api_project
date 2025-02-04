from django.db import models

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type_of_document = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    date = models.DateField()
    paid = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    description = models.TextField()
    image_id = models.CharField(max_length=255, blank=True, null=True)  # References PDF filenames