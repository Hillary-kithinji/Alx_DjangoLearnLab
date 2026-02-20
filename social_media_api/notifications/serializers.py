from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_title = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_title', 'read', 'timestamp']

    def get_target_title(self, obj):
        if hasattr(obj.target, 'title'):
            return obj.target.title
        return None