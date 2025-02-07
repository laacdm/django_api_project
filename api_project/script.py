# from records.models import Record
# from pdf2image import convert_from_path
# import os

# MEDIA_ROOT = "/home/laacdm/django_api_project/media/"
# THUMBNAIL_DIR = os.path.join(MEDIA_ROOT, "thumbnails")

# # Ensure thumbnail directory exists
# os.makedirs(THUMBNAIL_DIR, exist_ok=True)

# for record in Record.objects.all():
#     if record.image_id and not record.thumbnail:
#         pdf_path = os.path.join(MEDIA_ROOT, record.image_id)
#         thumbnail_path = os.path.join(THUMBNAIL_DIR, f"{os.path.splitext(record.image_id)[0]}.jpg")

#         if os.path.exists(pdf_path):
#             images = convert_from_path(pdf_path, first_page=1, last_page=1)
#             if images:
#                 images[0].save(thumbnail_path, "JPEG")
#                 record.thumbnail = f"thumbnails/{os.path.splitext(record.image_id)[0]}.jpg"
#                 record.save(update_fields=['thumbnail'])

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# user = User.objects.get(username="laac")  # Replace with your actual admin username
# token, created = Token.objects.get_or_create(user=user)
# print(f"Your API Token: {token.key}")

# from records.models import Record
# import os

# for record in Record.objects.all():
#     if record.image_id and not record.thumbnail:
#         record.thumbnail = f"thumbnails/{os.path.splitext(record.image_id)[0]}.jpg"
#         record.save(update_fields=['thumbnail'])

# print("✅ Thumbnails updated successfully!")

# from records.models import Record
# from pdf2image import convert_from_path
# import os

# MEDIA_ROOT = "/home/laacdm/django_api_project/media/"
# THUMBNAIL_DIR = os.path.join(MEDIA_ROOT, "thumbnails")

# Ensure the thumbnails directory exists
# os.makedirs(THUMBNAIL_DIR, exist_ok=True)

# record = Record.objects.get(image_id="IMG0064.pdf")
# pdf_path = os.path.join(MEDIA_ROOT, record.image_id)
# thumbnail_path = os.path.join(THUMBNAIL_DIR, f"{os.path.splitext(record.image_id)[0]}.jpg")

# if os.path.exists(pdf_path):
#     images = convert_from_path(pdf_path, first_page=1, last_page=1)
#     if images:
#         images[0].save(thumbnail_path, "JPEG")
#         record.thumbnail = f"thumbnails/{os.path.splitext(record.image_id)[0]}.jpg"
#         record.save(update_fields=['thumbnail'])

# print(f"✅ Fixed Thumbnail: {record.thumbnail}")

from records.models import Record

record = Record.objects.get(thumbnail="thumbnails/IMG0064.jpg")

print(f"Record Name: {record.name}")
print(f"PDF Path (image_id): {record.image_id}")
print(f"Thumbnail Path: {record.thumbnail}")
