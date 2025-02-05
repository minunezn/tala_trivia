from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TriviaViewSet

router = DefaultRouter()
router.register(r'', TriviaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('answer/<int:trivia_id>/<int:question_id>/', TriviaViewSet.as_view({'post': 'answer_question'}))

]
