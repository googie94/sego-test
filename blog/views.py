from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_detail(request):
    return render(request, 'blog/post_detail.html', {})

# Create your views here.
