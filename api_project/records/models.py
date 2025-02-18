from django.db import models
from pdf2image import convert_from_path
import os

# Define the media directories for PDFs and thumbnails
MEDIA_ROOT = "media"
THUMBNAILS_DIR = os.path.join(MEDIA_ROOT, "thumbnails")

# Ensure the thumbnails directory exists
os.makedirs(THUMBNAILS_DIR, exist_ok=True)


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
    image_id = models.CharField(max_length=255, blank=True, null=True)  # PDF filename
    thumbnail = models.CharField(max_length=255, blank=True, null=True)  # Thumbnail filename

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_thumbnail()

    def generate_thumbnail(self):
        """Generate a thumbnail from a PDF file if it doesn't already exist."""
        if self.image_id and not self.thumbnail:
            pdf_path = os.path.join(MEDIA_ROOT, self.image_id)
            thumbnail_filename = f"{os.path.splitext(self.image_id)[0]}.jpg"
            thumbnail_path = os.path.join(THUMBNAILS_DIR, thumbnail_filename)

            if os.path.exists(pdf_path):
                try:
                    # Convert first page of PDF to image
                    images = convert_from_path(pdf_path, first_page=1, last_page=1)
                    if images:
                        images[0].save(thumbnail_path, "JPEG")
                        self.thumbnail = f"thumbnails/{thumbnail_filename}"
                        super().save(update_fields=['thumbnail'])
                except Exception as e:
                    print(f"Error generating thumbnail for {pdf_path}: {e}")


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
        self.generate_thumbnail()

    def generate_thumbnail(self):
        """Generate a thumbnail from a PDF file if it doesn't already exist."""
        if self.image_id and not self.thumbnail:
            pdf_path = os.path.join(MEDIA_ROOT, self.image_id)
            thumbnail_filename = f"{os.path.splitext(self.image_id)[0]}.jpg"
            thumbnail_path = os.path.join(THUMBNAILS_DIR, thumbnail_filename)

            if os.path.exists(pdf_path):
                try:
                    # Convert first page of PDF to image
                    images = convert_from_path(pdf_path, first_page=1, last_page=1)
                    if images:
                        images[0].save(thumbnail_path, "JPEG")
                        self.thumbnail = f"thumbnails/{thumbnail_filename}"
                        super().save(update_fields=['thumbnail'])
                except Exception as e:
                    print(f"Error generating thumbnail for {pdf_path}: {e}")