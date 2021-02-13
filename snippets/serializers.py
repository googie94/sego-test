from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
가장 저단계 Serializer
"""
# class SnippetSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	code = serializers.CharField(style={'base_template': 'textarea.html'})
# 	linenos = serializers.BooleanField(required=True)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# 	def create(self, validated_data):
# 		"""
# 		검증된 데이터가 주어지면 새 'Snippet' 인스턴스를 만들고 반환합니다.
# 		"""
# 		return Snippet.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		"""
# 		검증된 데이터가 주어지면 새 'Snippet' 인스턴스를 업데이트하고 반환합니다.
# 		"""
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.code = validated_data.get('code', instance.code)
# 		instance.linenos = validated_data.get('linenos', instance.linenos)
# 		instance.language = validated_data.get('language', instance.language)
# 		instance.style = validated_data.get('style', instance.style)
# 		instance.save()
# 		return instance

"""
ModelSerilaizers를 이용한 단계
대단한 게 아니다. 다만, 저수준에서의 create 나 update를 구현해주는 편한 도구일 뿐
"""	
class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code', 'linenos', 'language', 'style']





