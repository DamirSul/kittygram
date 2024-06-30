# # Обновлённый urls.py
from django.urls import path, include

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]

from rest_framework.routers import SimpleRouter
from cats.views import CatViewSet


router = SimpleRouter()


# создание эндпоинтов
router.register('cats', CatViewSet) # cats/ and cats/<int:pk>/ CRUD


# включение эндпоинтов
urlpatterns = [
    path('', include(router.urls))
]