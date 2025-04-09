from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PagamentoViewSet

router = DefaultRouter()
router.register(r'pagamentos', views.PagamentoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
    path('pagamentos/novo/', views.criar_pagamentos, name='criar_pagamentos'),
    path('pagamentos/<int:id>/', views.detalhes_pagamento, name='detalhes_pagamento'),
    path('pagamentos/<int:id>/editar/', views.editar_pagamentos, name='editar_pagamentos'),
    path('pagamentos/<int:id>/excluir/', views.excluir_pagamentos, name='excluir_pagamentos'),
    path('relatorios/', views.relatorios, name='relatorios'),
    # Rotas da API REST
    path('', include(router.urls)),
]
