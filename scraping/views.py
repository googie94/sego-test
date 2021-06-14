from django.shortcuts import render
# 
from django.utils import timezone
import re
from konlpy.tag import Okt
from collections import Counter
# 
from rest_framework import viewsets
from .models import NaverPost, InstaPost, InstaTag
from .serializers import NaverPostSerializer, InstaPostSerializer

# Create your views here.

class NaverPostViewSet(viewsets.ModelViewSet):
    queryset = NaverPost.objects.all()
    serializer_class = NaverPostSerializer

class InstaPostViewSet(viewsets.ModelViewSet):
    queryset = InstaPost.objects.all()
    serializer_class = InstaPostSerializer


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
	for r in result:
		print(r[0])


	return render(request, 'scraping/insta.html', {'tags': result})