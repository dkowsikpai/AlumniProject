from rest_framework import serializers
from forum.models import Posts


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'
