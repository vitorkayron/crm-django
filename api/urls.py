from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

app_name = 'api'

urlpatterns = [
    path('', views.ProdutoList.as_view()),
    path('<int:pk>/', views.ProdutoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)