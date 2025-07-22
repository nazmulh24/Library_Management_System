from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from rest_framework import permissions
from circulation.permissions import IsLibrarian, IsMember
from circulation.models import BorrowRecord
from circulation.serializers import BorrowRecordSerializer
from drf_yasg.utils import swagger_auto_schema


class BorrowRecordViewSet(ModelViewSet):
    """
    Manage book borrowing records with CRUD operations
    - Librarians: Full access to all records
    - Members: Access only to their own borrow records
    - Custom endpoint: return/ (mark book as returned, calculate fines)
    """

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return BorrowRecord.objects.all()
        return BorrowRecord.objects.filter(member=user.member_profile)

    serializer_class = BorrowRecordSerializer

    @swagger_auto_schema(operation_summary="Retrieve a list of borrow records")
    def list(self, request, *args, **kwargs):
        """Retrieve borrow records based on user permissions"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new borrow record",
        operation_description="Create a new book borrowing record",
        request_body=BorrowRecordSerializer,
        responses={201: BorrowRecordSerializer, 400: "Bad Request"},
    )
    def create(self, request, *args, **kwargs):
        """Create a new borrow record"""
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Return a borrowed book",
        operation_description="Mark a book as returned, update available copies, and calculate fines if overdue",
        responses={
            200: "Book returned successfully",
            400: "Bad Request",
            404: "Not Found",
        },
    )
    @action(detail=True, methods=["post"], url_path="return")
    def return_book(self, request, pk=None):
        """
        Custom action to return a borrowed book:
        - Sets return_date to today
        - Marks is_returned = True
        - Increments the book's available_copies
        - Calculates fine if overdue and creates a Fine record
        """

        try:
            # Retrieve the BorrowRecord instance (borrow)
            borrow = self.get_object()

            # Check if already returned
            if borrow.is_returned:
                return Response(
                    {"message": "Book is already returned."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Set return_date and mark returned
            borrow.return_date = timezone.now().date()
            borrow.is_returned = True
            borrow.save()

            # Increase the available copies of the book
            book = borrow.book
            book.available_copies += 1
            book.save()

            # Fine calculation if returned late
            fine_amount = 0
            if borrow.return_date > borrow.due_date:
                days_late = (borrow.return_date - borrow.due_date).days
                fine_amount = days_late * 10  # e.g., 10 taka per day late

                # Create Fine record
                Fine.objects.create(
                    borrow_record=borrow,
                    amount=fine_amount,
                )

            # Return success response with details
            return Response(
                {
                    "id": borrow.id,
                    "message": "Book returned successfully.",
                    "return_date": str(borrow.return_date),
                    "is_returned": borrow.is_returned,
                    "fine_amount": fine_amount,
                },
                status=status.HTTP_200_OK,
            )

        except BorrowRecord.DoesNotExist:
            # This should rarely happen because get_object() raises 404 automatically,
            # but included for completeness.
            return Response(
                {"error": "Borrow record not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
