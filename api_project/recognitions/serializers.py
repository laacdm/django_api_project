from rest_framework import serializers
from .models import Recognition

class RecognitionSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Recognition
        fields = [
            'recognition_id', 'name', 'type_of_recognition', 'institution', 'date', 'pdf_url', 'thumbnail_url'
        ]

    def get_pdf_url(self, obj):
        """Returns the full URL for the PDF file."""
        request = self.context.get('request')
        if obj.image_id:
            return request.build_absolute_uri(f'/media/{obj.image_id}')
        return None

    def get_thumbnail_url(self, obj):
        """Returns the full URL for the thumbnail image."""
        request = self.context.get('request')
        if obj.thumbnail:
            return request.build_absolute_uri(f'/media/{obj.thumbnail}')
        return None
