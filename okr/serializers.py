from rest_framework import serializers
from .models import Team, User, Objective, KeyResult, OkrProgress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth=1
        fields = ['id', 'name', 'team']

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        depth=1
        fields = ['id', 'title', 'rate', 'data_type', 'team', 'leader', 'type', 'create_date', 'end_date']

class TeamSerializer(serializers.ModelSerializer):
    objective_team = ObjectiveSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        depth=1
        fields = ['id', 'name', 'objective_team']

class KeyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyResult
        depth=1
        fields = ['id', 'objective', 'title', 'user', 'type_data', 'obtained', 'expected', 'percentage', 'create_date']

class OkrProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OkrProgress
        fields = ['id', 'progress', 'memo', 'create_date', 'key_result']







