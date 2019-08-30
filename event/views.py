# Create your views here.
from .models import EventBooking, EventSeatClass
from .serializers import EventBookingSerializer, EventBookingListSerializer, EventSeatClassSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict
from core.api_permission import UserAuthentication


class EventBookingViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for event booking
    """
    lookup_field = 'id'
    model = EventBooking
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
    permission_classes = (UserAuthentication,)

    def list(self, request):
        """
            To list the event booking
            URL Structure: /event/book/
            Required Fields: None
        """

        queryset = self.model.objects.filter(user=request.user, active=True)

        serializer = EventBookingListSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
            To create the movie booking
            URL Structure: /movie/book/
            Required Fields: 'user', 'event', 'seat_class', 'seat_number', 'no_of_tickets'
        """

        data = QueryDict.dict(request.data)
        data['user'] = request.user.pk
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            obj = serializer.save()

            obj.service_fee = obj.no_of_tickets * 30
            obj.total_cost = obj.service_fee + (obj.no_of_tickets * obj.seat_class.cost_per_ticket)

            obj.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id, *args, **kwargs):
        """
            To update the particular event booked
            URL Structure: /event/book/1/
            Required Fields: `id`, 'user', 'event', 'seat_class', 'seat_number', 'no_of_tickets', 'service_fee', 'total_cost'
        """

        try:
            queryset = self.model.objects.get(id=id, active=True)
        except:
            return Response({'message': 'Not exist'}, status=400)
        data = QueryDict.dict(request.data)
        data['user'] = request.user.pk
        serializer = self.serializer_class(queryset, data=data, partial=True)

        if serializer.is_valid():
            obj = serializer.save()

            obj.service_fee = obj.no_of_tickets * 30
            obj.total_cost = obj.service_fee + (obj.no_of_tickets * obj.seat_class.cost_per_ticket)

            obj.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, *args, **kwargs):
        """
            To delete the particular event booked
            URL Structure: /event/book/1/
            Required Fields: id
        """
        try:
            queryset = self.model.objects.get(id=id, active=True)
        except:
            return Response({'message': 'Not exist'}, status=400)

        queryset.active = False
        queryset.save()

        return Response({'message': 'Deleted'}, status=200)