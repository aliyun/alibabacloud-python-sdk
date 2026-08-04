# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateMemberSubscriptionRequest(DaraModel):
    def __init__(
        self,
        amount: float = None,
        balance_type: str = None,
        effective_time: int = None,
        idempotency_key: str = None,
    ):
        # The subscription amount.
        self.amount = amount
        # The balance type. Valid values:
        # 
        # - permanent: permanent balance.
        # - monthly: monthly balance.
        self.balance_type = balance_type
        # The effective period in UNIX timestamp (seconds).
        self.effective_time = effective_time
        # The idempotency key. UUID v4 format is recommended.
        self.idempotency_key = idempotency_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.idempotency_key is not None:
            result['idempotencyKey'] = self.idempotency_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('idempotencyKey') is not None:
            self.idempotency_key = m.get('idempotencyKey')

        return self

