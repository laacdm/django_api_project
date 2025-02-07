from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = [
            'record_id', 'name', 'type_of_document', 'institution', 'specialization',
            'date', 'paid', 'provider', 'description', 'pdf_url', 'thumbnail_url'
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
