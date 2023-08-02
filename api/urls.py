from django.urls import path
from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version="v1",
        description="API for Products, Sales, and Balance",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swagger.Blog.local"),
        license=openapi.License(name="Test License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('produto/', views.ProdutoList.as_view(), name='produto-list'),
    path('produto/<int:pk>/', views.ProdutoDetail.as_view(), name='produto-detail'),
    path('venda/', views.VendaList.as_view(), name='venda-list'),
    path('venda/<int:pk>', views.VendaDetail.as_view(), name='venda-detail'),
    path('saldo/', views.SaldoList.as_view(), name='saldo-detail'),
    path('saldo/<int:pk>', views.SaldoDetail.as_view(), name='saldo-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
]