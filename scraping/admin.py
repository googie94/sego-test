from django.contrib import admin
from .models import PostNaver, PostNaverImage, PostNaverTag, PostInstagram, PostInstagramTag

@admin.register(PostNaver)
class PostNaverAdmin(admin.ModelAdmin):
	list_display = ('created_date', 'author', 'title',)
	ordering = ('-created_date',)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		qs = qs.order_by('-created_date').defer('content',)
		return qs

@admin.register(PostInstagram)
class PostInstagramAdmin(admin.ModelAdmin):
	list_display = ('created_date', 'author', 'content',)
	ordering = ('-created_date',)

@admin.register(PostInstagramTag)
class PostInstagramTagAdmin(admin.ModelAdmin):
	list_display = ('tag',)