from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']