from rest_framework import serializers

from .models import Email


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ('from_email', 'to_email', 'subject', 'content')
