from rest_framework import serializers
from .models import NaverPost, InstaPost, InstaTag
from .models import PostNaver, PostNaverImage, PostNaverTag, PostInstagram, PostInstagramTag
# 
from collections import Counter


class PostNaverSerializer(serializers.ModelSerializer):
	pictures = serializers.SerializerMethodField('get_pictures')
	tags = serializers.SerializerMethodField('get_tags')

	def get_pictures(self, post):
		post_id = post.post_id
		queryset = PostNaverImage.objects.filter(post_id=post_id)
		serializer = PostNaverImageSerializer(instance=queryset, many=True)
		return serializer.data

	def get_tags(self, post):
		post_id = post.post_id
		queryset = PostNaverTag.objects.filter(post_id=post_id)
		serializer = PostNaverTagSerializer(instance=queryset, many=True)
		return serializer.data

	class Meta:
		model = PostNaver
		fields = '__all__'

class PostNaverImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostNaverImage
		fields = '__all__'

class PostNaverTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostNaverTag
		fields = '__all__'

class MostPostNaverTagSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField()
	class Meta:
		model = PostNaverTag
		fields = ('tag', 'count')

class PostInstagramSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostInstagram
		fields = '__all__'

class PostInstagramTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostInstagramTag
		fields = '__all__'

class MostPostInstagramTagSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField()
	class Meta:
		model = PostInstagramTag
		fields = ('tag', 'count')


######################################################

class NaverPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = NaverPost
		fields = ['id', 'post_id', 'category', 'title', 'content', 'created_date', 'link']

class InstaPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = InstaPost
		fields = ['id', 'short_code', 'content', 'created_date', 'like_count']

class InstaTagSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField()
	class Meta:
		model = InstaTag
		fields = ['tag', 'count']