from dataclasses import fields
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import WorkerSerializer, SalesPointSerializer, VisitingSerializer
from .models import Worker, SalesPoint, Visiting

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class SalesPointViewSet(viewsets.ModelViewSet):
    queryset = SalesPoint.objects.all()
    serializer_class = SalesPointSerializer


    def get(self, request):
        phone = request.GET.get('phone', '')
        queryset = SalesPoint.objects.filter(worker__phone=phone).all()
        serializer = SalesPointSerializer(queryset, many=True)
        return Response(serializer.data)

class VisitingViewSet(viewsets.ModelViewSet):
    queryset = Visiting.objects.all()
    serializer_class = VisitingSerializer
    
    def get(self, request):
        queryset = Visiting.objects.filter(sales_point__worker__phone=request.GET.get('phone', None)).all()
        serializer = VisitingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        phone = request.GET.get('phone', None)
        if phone:
            if SalesPoint.objects.get(pk=request.data['sales_point']).worker.phone == phone:
                serializer = VisitingSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    visit = serializer.save()
                return Response({"sales_point":visit.pk, "date":visit.date})
            else:
                return Response({'Invalid phone.'}, status=403)
        else:
            return Response({'Phone not found. Specify the phone number in the request parameters.'}, status=401)


