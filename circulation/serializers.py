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


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = "__all__"
        read_only_fields = [
            "id",
            "member",
            "borrow_date",
            "due_date",
            "is_returned",
            "return_date",
        ]

    def validate(self, data):
        book = data.get("book")
        if book and book.available_copies < 1:
            raise serializers.ValidationError(
                "This book is not available for borrowing."
            )
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        member = getattr(user, "member_profile", None)

        if not member:
            raise serializers.ValidationError("Only members can borrow books.")

        book = validated_data.get("book")
        if book.available_copies < 1:
            raise serializers.ValidationError("This book is not available.")

        # --> Decrease available copies
        book.available_copies -= 1
        book.save()

        # --> Create record
        borrow_record = BorrowRecord.objects.create(
            member=member,
            book=book,
        )
        return borrow_record
