from rest_framework import serializers

from circulation.models import BorrowRecord
from catalog.models import Book
from users.models import Member

from datetime import timedelta
from django.utils import timezone


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = [
            "id",
            "member",
            "book",
            "borrow_date",
            "due_date",
            "is_returned",
        ]

    def validate(self, data):
        book = data["book"]
        if book.available_copies < 1:
            raise serializers.ValidationError(
                "This book is not available for borrowing."
            )
        return data

    def create(self, validated_data):
        book = validated_data["book"]
        book.available_copies -= 1
        book.save()

        validated_data["due_date"] = timezone.now().date() + timedelta(days=14)
        return super().create(validated_data)


class ReturnSerializer(serializers.Serializer):
    borrow_id = serializers.IntegerField()

    def validate(self, data):
        try:
            borrow = BorrowRecord.objects.get(id=data["borrow_id"])
        except BorrowRecord.DoesNotExist:
            raise serializers.ValidationError("Borrow record does not exist.")

        if borrow.is_returned:
            raise serializers.ValidationError("Book is already returned.")
        return data

    def save(self, **kwargs):
        borrow = BorrowRecord.objects.get(id=self.validated_data["borrow_id"])
        borrow.return_date = timezone.now().date()
        borrow.is_returned = True
        borrow.book.available_copies += 1
        borrow.book.save()
        borrow.save()

        if borrow.return_date > borrow.due_date:
            from circulation.models import Fine

            days_late = (borrow.return_date - borrow.due_date).days
            fine_amount = days_late * 10  # --> 10 taka fine per day
            Fine.objects.create(
                borrow_record=borrow,
                amount=fine_amount,
            )

        return borrow
