from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from django.utils import timezone
from datetime import timedelta

from rest_framework import permissions
from circulation.permissions import IsLibrarian, IsMember
from circulation.models import BorrowRecord
from circulation.serializers import (
    BorrowSerializer,
    ReturnSerializer,
    BorrowRecordSerializer,
)


class BorrowViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        if book.available_copies < 1:
            raise ValidationError("This book is not available for borrowing.")

        book.available_copies -= 1
        book.save()

        due_date = timezone.now().date() + timedelta(days=14)
        serializer.save(due_date=due_date)


class ReturnBookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReturnSerializer(data=request.data)
        if serializer.is_valid():
            borrow = serializer.save()
            return Response(
                {"detail": "Book returned successfully."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BorrowRecordViewSet(ModelViewSet):
    serializer_class = BorrowRecordSerializer
    # permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ["update", "partial_update", "destroy"]:
    #         return [IsLibrarian()]
    #     return [IsMember()]
    def get_permissions(self):
        if self.action in ["create"]:
            return [IsMember()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsLibrarian()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return BorrowRecord.objects.all()
        return BorrowRecord.objects.filter(member=user.member_profile)

    def perform_create(self, serializer):
        serializer.save(member=self.request.user.member_profile)
