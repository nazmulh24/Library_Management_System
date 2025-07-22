from django.db import models
from users.models import Member
from catalog.models import Book

from datetime import timedelta, time, datetime
from django.utils import timezone


def default_due_date():
    return timezone.now().date() + timedelta(days=14)


class BorrowRecord(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="borrowed_books",
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrow_records",
    )
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=default_due_date)
    return_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)

    @property
    def fine_amount(self):
        return self.fine.amount if hasattr(self, "fine") else 0.00

    def __str__(self):
        return f"{self.member} borrowed {self.book}"

    class Meta:
        ordering = ["-borrow_date"]


class Fine(models.Model):
    borrow_record = models.OneToOneField(
        BorrowRecord,
        on_delete=models.CASCADE,
        related_name="fine",
    )
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Fine for {self.borrow_record} - {'Paid' if self.paid else 'Unpaid'}"
