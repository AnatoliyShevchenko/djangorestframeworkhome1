from django.db.models import QuerySet

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from typing import Optional

from .models import Car
from .serializers import CarSerializer

# Create your views here.
class CarView(ViewSet):
    """Car View."""

    queryset = Car.objects.all()

    def list(
        self, 
        request: Request, 
        *args, 
        **kwargs
    ) -> Response:
        cars: QuerySet[Car] = self.queryset.all()
        serializer: CarSerializer = \
        CarSerializer(
            cars,
            many=True
        )
        return Response({"result" : serializer.data}, status=200)

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET Method. get some object."""

        user: Optional[Car] = None
        try:
            user = self.queryset.get(
                id=pk
            )
            serializer: CarSerializer = \
            CarSerializer(user)
        except Car.DoesNotExist:
            return Response({
                'message': 'error'
            })
        else:
            return Response({
                'data': {
                    'car': serializer.data
                }
            })