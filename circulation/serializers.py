from rest_framework import serializers

from circulation.models import BorrowRecord

<<<<<<< HEAD
from datetime import date
=======
from datetime import timedelta, date
from django.utils import timezone
>>>>>>> old-state


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
<<<<<<< HEAD
        if obj.is_returned:
            return 0

        today = date.today()
        if obj.due_date and today > obj.due_date:
            delta = (today - obj.due_date).days
            fine_per_day = 10  # ---> example: 10 BDT per day
            return delta * fine_per_day
        return 0
=======
        if hasattr(obj, "fine") and obj.fine:
            return obj.fine.amount
        return 0.0
>>>>>>> old-state

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
