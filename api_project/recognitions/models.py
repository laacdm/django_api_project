from django.db import models
from pdf2image import convert_from_path
import os

class Recognition(models.Model):
    recognition_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type_of_recognition = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    date = models.DateField()
    image_id = models.CharField(max_length=255, blank=True, null=True)  # PDF filename
    thumbnail = models.CharField(max_length=255, blank=True, null=True)  # Thumbnail filename

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Generate a thumbnail for the PDF
        if self.image_id and not self.thumbnail:
            pdf_path = os.path.join('media', self.image_id)
            thumbnail_path = os.path.join('media', 'thumbnails', f"{os.path.splitext(self.image_id)[0]}.jpg")

            if os.path.exists(pdf_path):
                images = convert_from_path(pdf_path, first_page=1, last_page=1)
                if images:
                    images[0].save(thumbnail_path, "JPEG")
                    self.thumbnail = f"thumbnails/{os.path.splitext(self.image_id)[0]}.jpg"
                    super().save(update_fields=['thumbnail'])