from uuid import uuid4

from django.db import models

from src.mextalki.models.base_model import TimeStampMixin


class PlanPayment(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name='plan_payments',
        blank=False,
        null=False,
    )
    plan = models.ForeignKey(
        'mextalki.Plan',
        on_delete=models.PROTECT,
        related_name='payment',
        blank=False,
        null=False,
    )
    paypal_payment = models.ForeignKey(
        'paypal.PaypalPayment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{id}'.format(id=self.id)

    class Meta:
        ordering = ['-created_at']
