from rest_framework import serializers

from status_app.models import Status


class StatusSerializer(serializers.ModelSerializer):
    """
    Serializer for Status Model
    """

    class Meta:
        model = Status
        fields = [
            'id', 'user', 'content', 'image'
        ]
        read_only = ['id']

    # def validate_content(self, value):
    #     if len(value) > 64:
    #         raise serializers.ValidationError("Content must be less than 64 Characters")
    #     return value

    def validated(self, data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            serializers.ValidationError('Image or Content are required Field')
        return data
