from rest_framework import serializers

from status_app.models import Status


class StatusSerializer(serializers.ModelSerializer):
    """
    Serializer for Status Model
    """

    # user = serializers.HyperlinkedRelatedField(lookup_field='id', read_only=True,
    #                                            view_name='accounts:user_details')
    user_details = serializers.HyperlinkedRelatedField(source='user', lookup_field='id', read_only=True,
                                                       view_name='accounts:user_details')
    username = serializers.SlugRelatedField(source='user', read_only='True', slug_field='email')

    class Meta:
        model = Status
        fields = [
            'id', 'user', 'content', 'image', 'username', 'user_details'
        ]
        read_only = ['id']

    # def validate_content(self, value):
    #     if len(value) > 64:
    #         raise serializers.ValidationError("Content must be less than 64 Characters")
    #     return value

    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Image or Content are required Field')
        return data
