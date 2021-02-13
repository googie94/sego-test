from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse, Http404
# from django.views.decorators.csrf import csrf_exempt
# #
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
# from rest_framework.views import APIView
# #
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

"""
#요청
request.POST = 오직 form data만 처리합니다. POST 메소드만 처리합니다.
request.data = 임의의 데이터를 다룹니다. POST, PUT, PATCH 메소를 처리합니다.
#응답
return Response(data) = 요청된 클라이언트의 콘텐츠 유형으로 반환됩니다.
#상태
HTTP로 보낸다 해서 모두 다 처리하는 것은 아닙니다. 잘못된 입력은 오류를 일으킵니다.
HTTP_400_BAD_REQUEST와 같이 식별자를 정해 사용하면 좋습니다.
#API래핑
@api_view 혹은 클래스 기반의 APIView 를 사용할 수 있습니다.
이는 request에서 인스턴스를 수신하는 지 확인하고 콘텐츠를 올바르게 추가하는 것에 도움을 줍니다.
"""

# class SnippetList(APIView):
	"""
	모든 코드 스니펫(조각)을 나열하거나, 새롭게 만듭니다
	"""
# @csrf_exempt #토큰 없는 클라이언트가 POST 할 수 있게 헤준다. 보편적으로 이런 일은 없다
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
	"""
	모든 코드 스니펫(조각)을 나열하거나, 새롭게 만듭니다
	"""
	# if request.method == 'GET':
	# 	snippets = Snippet.objects.all()
	# 	serializer = SnippetSerializer(snippets, many=True)
	# 	return JsonResponse(serializer.data, safe=False)

	# elif request.method == 'POST':
	# 	data = JSONParser().parse(request)
	# 	serializer = SnippetSerializer(data=data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return JsonResponse(serializer.data, status=201)
	# 	return JsonResponse(serializer.errors, status=400)
	#----리팩토링 전------#
	# if request.method == "GET":
	# 	snippets = Snippet.objects.all()
	# 	serializer = SnippetSerializer(snippets, many=True)
	# 	return Response(serializer.data)
	# elif request.method == "POST":
	# 	serializer = SnippetSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=statsus.HTTP_400_REQUEST)


# @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request, pk, format=None):
	"""
	스니펫을 검색,업데이트,삭제합니다
	"""
	# try:
	# 	snippet = Snippet.objects.get(pk=pk)
	# except Snippet.DoesNotExist:
	# 	return HttpResponse(status=404)

	# if request.method == 'GET':
	# 	serializer = SnippetSerializer(snippet)
	# 	return JsonResponse(serializer.data)

	# elif request.method == 'PUT':
	# 	data = JSONParser().parse(request)
	# 	serializer = SnippetSerializer(snippet, data=data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return JsonResponse(serializer.data)
	# 	return JsonResponse(serializer.errors, status=400)

	# elif request.method == 'DELETE':
	# 	snippet.delete()
	# 	return HttpResponse(status=204)
	#----리팩토링 전------#
	# try:
	# 	snippet = Snippet.objects.get(pk=pk)
	# except Snippet.DoesNotExist:
	# 	return Response(stastus=status.HTTP_404_NOT_FOUND)
	# if request.method == 'GET':
	# 	serializer = SnippetSerializer(snippet)
	# 	return Response(serializer.data)

	# elif request.method == 'PUT':
	# 	serializer = SnippetSerializer(snippet, data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# elif request.method == 'DELETE':
	# 	snippet.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)



