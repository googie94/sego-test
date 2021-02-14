from blog.models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ['id', 'title', 'text', 'created_date', 'author', 'approved_post', 'comments']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	posts = PostSerializer(many=True, read_only=True)
	class Meta:
		model = Comment
		fields = ['id', 'author', 'text', 'created_date', 'post_id', 'approved_comment', 'posts']


