from rest_framework import serializers

from communication.models import Feedback


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ['url', 'supplier', 'name', 'email', 'image', 'message']
