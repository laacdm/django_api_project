from records.models import Record
from pdf2image import convert_from_path
import os

MEDIA_ROOT = "/home/laacdm/django_api_project/media/"
THUMBNAIL_DIR = os.path.join(MEDIA_ROOT, "thumbnails")

# Ensure thumbnail directory exists
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

for record in Record.objects.all():
    if record.image_id and not record.thumbnail:
        pdf_path = os.path.join(MEDIA_ROOT, record.image_id)
        thumbnail_path = os.path.join(THUMBNAIL_DIR, f"{os.path.splitext(record.image_id)[0]}.jpg")

        if os.path.exists(pdf_path):
            images = convert_from_path(pdf_path, first_page=1, last_page=1)
            if images:
                images[0].save(thumbnail_path, "JPEG")
                record.thumbnail = f"thumbnails/{os.path.splitext(record.image_id)[0]}.jpg"
                record.save(update_fields=['thumbnail'])
