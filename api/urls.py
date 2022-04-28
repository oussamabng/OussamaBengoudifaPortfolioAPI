from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('portfolio', PortfolioViewSet,basename='portfolios')
router.register('jobs_title', JobTitleViewSet,basename='jobs_title')
router.register('languages', LanguageViewSet,basename='languages')
router.register('skills', SkillViewSet,basename='skills')
router.register('educations', EducationViewSet,basename='educations')
router.register('experiences', ExperienceViewSet,basename='experiences')
router.register('project_types', ProjectTypeViewSet,basename='project_types')
router.register('projects', ProjectViewSet,basename='projects')
router.register('stacks', StackViewSet,basename='stacks')
router.register('uploads', UploadViewSet,basename='uploads')

urlpatterns = router.urls
