from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from circulation.models import BorrowRecord, Fine
from catalog.models import Book
from users.models import Member

from datetime import timedelta
from django.utils import timezone


class BorrowRecordSerializer(serializers.ModelSerializer):
    fine_amount = serializers.SerializerMethodField()

    class Meta:
        model = BorrowRecord
        fields = [
            "id",
            "member",
            "book",
            "borrow_date",
            "due_date",
            "fine_amount",
            "is_returned",
            "return_date",
        ]
        read_only_fields = [
            "id",
            "member",
            "borrow_date",
            "due_date",
            "fine_amount",
            "is_returned",
            "return_date",
        ]

    def get_fine_amount(self, obj):
        if hasattr(obj, "fine") and obj.fine:
            return obj.fine.amount
        return 0.0

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


class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = [
            "id",
            "borrow_record",
            "amount",
            "paid",
            "paid_at",
        ]
        read_only_fields = ["borrow_record", "amount", "paid_at"]
