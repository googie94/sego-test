from django.shortcuts import render
#
from rest_framework import viewsets
from django.views import generic
from .serializers import TeamSerializer, UserSerializer, ObjectiveSerializer, KeyResultSerializer, OkrProgressSerializer
#
from .models import Team, User, Objective, KeyResult, OkrProgress
from .forms import TeamForm, UserForm, ObjectiveForm, KeyResultForm, OkrProgressForm
#

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer

class KeyResultViewSet(viewsets.ModelViewSet):
    queryset = KeyResult.objects.all()
    serializer_class = KeyResultSerializer

class OkrProgressViewSet(viewsets.ModelViewSet):
    queryset = OkrProgress.objects.all()
    serializer_class = OkrProgressSerializer


def OkrView(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'okr/index.html')










