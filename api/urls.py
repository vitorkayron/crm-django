from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version="v1",
        description="API for Products, Sales and Balance",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swagger.Blog.local"),
        license=openapi.License(name="Test License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('produto/', views.ProdutoList.as_view()),
    path('produto/<int:pk>/', views.ProdutoDetail.as_view()),
    path('venda/', views.VendaList.as_view()),
    path('produto/<int:pk>', views.VendaDetail.as_view()),
    path('saldo/', views.SaldoList.as_view()),
    path('saldo/<int:pk>', views.SaldoDetail.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name="schema_redoc")
]

urlpatterns = format_suffix_patterns(urlpatterns)