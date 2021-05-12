from rest_framework import serializers

from ..models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    """
        Create post and set request user as post author.
    """

    title = serializers.CharField(write_only=True, required=True)
    body = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Post
        fields = ('title', 'body')

    def create(self, validated_data):
        user =  self.context['request'].user
        post = Post.objects.create(
            title=validated_data['title'],
            body=validated_data['body'],
            author=user
        )

        post.save()
        return post

