from django.urls import include, path
from rest_framework import routers
from .views import WorkerViewSet, SalesPointViewSet, VisitingViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('worker/', WorkerViewSet.as_view({'get': 'list'})),
    path('sales_point/', SalesPointViewSet.as_view({'get': 'get'})),
    path('visiting/', VisitingViewSet.as_view({'post':'post'})),
    # path('visiting/', VisitingViewSet.as_view({'get':'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])