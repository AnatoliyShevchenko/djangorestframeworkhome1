from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Car

# Create your views here.
class CarView(APIView):
    """Car View."""

    def get(
        self, 
        request: WSGIRequest, 
        *args, 
        **kwargs
    ) -> Response:
        cars: QuerySet[Car] = Car.objects.all()
        result: list[dict[str, str]] = []
        for car in cars:
            result.append({
                "mark" : car.mark.mark_title,
                "model" : car.model.model_title,
                "color" : car.color.color_title,
                "year" : car.year_of_issue
            })
        return Response({"result" : result}, status=200)