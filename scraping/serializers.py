from rest_framework import serializers
from .models import NaverPost, InstaPost

class NaverPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = NaverPost
		fields = ['id', 'post_id', 'category', 'title', 'content', 'created_date', 'link']

class InstaPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = InstaPost
		fields = ['id', 'short_code', 'content', 'created_date', 'like_count']