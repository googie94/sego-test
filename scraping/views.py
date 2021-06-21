from django.shortcuts import render
# 
from django.utils import timezone
import re
from konlpy.tag import Okt
from collections import Counter
# 
from rest_framework import viewsets
from .models import NaverPost, InstaPost, InstaTag
from .serializers import NaverPostSerializer, InstaPostSerializer, InstaTagSerializer
from .models import PostNaver, PostNaverImage, PostNaverTag, PostInstagram, PostInstagramTag
from .serializers import PostNaverSerializer, PostNaverImageSerializer, PostNaverTagSerializer, MostPostNaverTagSerializer, PostInstagramSerializer, PostInstagramTagSerializer, MostPostInstagramTagSerializer

# Create your views here.

class PostNaverViewSet(viewsets.ModelViewSet):
	queryset = PostNaver.objects.all()
	serializer_class = PostNaverSerializer

	def get_queryset(self):
		queryset = super().get_queryset()
		for q in queryset:
			q.author = q.author.replace('\n', '')
			q.title = q.title.replace('\n', '')
		return queryset

class PostNaverImageViewSet(viewsets.ModelViewSet):
	queryset = PostNaverImage.objects.all()
	serializer_class = PostNaverImageSerializer

class PostNaverTagViewSet(viewsets.ModelViewSet):
	queryset = PostNaverTag.objects.all()
	serializer_class = PostNaverTagSerializer

	def get_queryset(self):
		return super().get_queryset()

class MostPostNaverTagViewSet(viewsets.ModelViewSet):
	queryset = PostNaverTag.objects.all()
	serializer_class = MostPostNaverTagSerializer

	def get_queryset(self):
		queryset = super().get_queryset()
		total = list()
		post_authors = list()
		posts = PostNaver.objects.all().exclude(author='\n플랩풋볼\n')
		for p in posts:
			post_authors.append(p.post_id)
		for q in queryset:
			if q.post_id in post_authors:
				if q.hangul() != '':
					total.append(q.hangul())
		counter = Counter(total)
		ignore = ['\n플랩풋볼\n']
		for x in ignore:
			del counter[x]
		result = counter.most_common(20)
		most_list = []
		for i in range(0,20):
			dt = {
				'tag': result[i][0],
				'count': result[i][1]
			}
			most_list.append(dt)
		return most_list

class PostInstagramViewSet(viewsets.ModelViewSet):
	queryset = PostInstagram.objects.all()
	serializer_class = PostInstagramSerializer

	def get_queryset(self):
		queryset = super().get_queryset()
		for q in queryset:
			q.content = q.content.replace('????', '')
		return queryset

class PostInstagramTagViewSet(viewsets.ModelViewSet):
	queryset = PostInstagramTag.objects.all()
	serializer_class = PostInstagramTagSerializer

	def get_queryset(self):
		return super().get_queryset()

class MostPostInstagramTagViewSet(viewsets.ModelViewSet):
	queryset = PostInstagramTag.objects.all()
	serializer_class = MostPostInstagramTagSerializer

	def get_queryset(self):
		queryset = super().get_queryset()
		total = list()
		post_authors = list()
		posts = PostInstagram.objects.all().exclude(author='7329956340')
		for p in posts:
			post_authors.append(p.post_id)
		for q in queryset:
			if q.post_id in post_authors:
				if q.hangul() != '':
					total.append(q.hangul())
		counter = Counter(total)
		ignore = ['플랩풋볼']
		for x in ignore:
			del counter[x]
		result = counter.most_common(20)
		most_list = []
		for i in range(0,20):
			dt = {
				'tag': result[i][0],
				'count': result[i][1]
			}
			most_list.append(dt)
		return most_list



############################################################# 

class NaverPostViewSet(viewsets.ModelViewSet):
    queryset = NaverPost.objects.all()
    serializer_class = NaverPostSerializer

class InstaPostViewSet(viewsets.ModelViewSet):
    queryset = InstaPost.objects.all()
    serializer_class = InstaPostSerializer

class InstaTagViewSet(viewsets.ModelViewSet):
	queryset = InstaTag.objects.all()
	serializer_class = InstaTagSerializer

	def get_queryset(self):
		queryset = super().get_queryset()
		total = list()
		for q in queryset:
			if q.hangul() != '':
				total.append(q.hangul())
		counter = Counter(total)
		result = counter.most_common(20)
		most_list = []
		for i in range(0,20):
			dt = {
				'tag': result[i][0],
				'count': result[i][1]
			}
			most_list.append(dt)
		return most_list


def scraping_home(request):
	posts = NaverPost.objects.all().order_by('-created_date')
	posts = list(posts)
	for index, post in enumerate(posts):
		if post.content == '':
			del posts[index]
		else:
			post.content = re.sub("(\[\[\[[A-Z])\D+([A-Z])\D\d\]\]\]", "", post.content)
	return render(request, 'scraping/home.html', {'posts': posts})

def scraping_detail(request, pk):
	post = NaverPost.objects.get(pk=pk)
	return render(request, 'scraping/detail.html', {'post': post})


def scraping_insta(request):
	tags = InstaTag.objects.all()

	# 
	total = list()
	for tag in tags:
		if tag.hangul() != '':
			total.append(tag.hangul())
	counter = Counter(total)
	result = counter.most_common(200)
	# print(result)
	# for r in result:
		# print(r[0])


	return render(request, 'scraping/insta.html', {'tags': result})