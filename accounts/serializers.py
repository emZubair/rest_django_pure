from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.reverse import reverse as api_reverse

from status_app.api.serializer import StatusSerializer


class UserDetailsSerializers(serializers.ModelSerializer):
    # status = serializers.HyperlinkedRelatedField(source='status_set', lookup_field='id',
    #                                              many=True, read_only=True,
    #                                              view_name='status:sim')

    status = StatusSerializer(source='status_set', many=True, read_only=True)
    # status_home = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username', 'status', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined',
            # 'status_home'
        )

    def get_status_home(self, obj):
        request = self.context.get('request')
        return api_reverse('status_app:list', request=request)
