# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateSubscriptionRequest(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        effective_time: int = None,
        idempotency_key: str = None,
        subscription_amount: float = None,
    ):
        # The balance pool to which the recharge is applied. Valid values:
        # - permanent: the permanent balance pool.
        # - monthly: the monthly balance pool.
        self.balance_type = balance_type
        # The effective period, in UNIX timestamp (seconds). Range: from 00:00 of today to 00:00 of the first day of the next month (Asia/Shanghai).
        self.effective_time = effective_time
        # The idempotency key. UUID v4 format without hyphens is recommended. This prevents duplicate subscription creation.
        self.idempotency_key = idempotency_key
        # The subscription recharge amount.
        self.subscription_amount = subscription_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.idempotency_key is not None:
            result['idempotencyKey'] = self.idempotency_key

        if self.subscription_amount is not None:
            result['subscriptionAmount'] = self.subscription_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('idempotencyKey') is not None:
            self.idempotency_key = m.get('idempotencyKey')

        if m.get('subscriptionAmount') is not None:
            self.subscription_amount = m.get('subscriptionAmount')

        return self

