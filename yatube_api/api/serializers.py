from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from django.shortcuts import get_object_or_404

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(read_only=True)
    description = serializers.StringRelatedField()

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError('На себя подписываться нельзя')
        if Follow.objects.filter(user=self.context['request'].user,
                                 following=data['following']).exists():
            raise serializers.ValidationError('Вы уже подписаны на '
                                              'этого пользователя')
        return data

    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    following = serializers.SlugRelatedField(
        slug_field='username', required=True, queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def create(self, validated_data):
        following = get_object_or_404(User,
                                      username=validated_data['following']
                                      )
        return Follow.objects.create(user=self.context['request'].user,
                                     following=following)
