# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterTransferToMemberRequest(DaraModel):
    def __init__(
        self,
        amount: float = None,
        balance_type: str = None,
        idempotency_key: str = None,
        monthly_quota: float = None,
        remark: str = None,
    ):
        # The transfer amount.
        self.amount = amount
        # The balance type. Valid values:
        # 
        # - permanent
        # - monthly
        # 
        # Default value: permanent.
        self.balance_type = balance_type
        # The idempotency key. UUID v4 format is recommended.
        self.idempotency_key = idempotency_key
        # The monthly refresh quota for monthly-type transfers.
        self.monthly_quota = monthly_quota
        # The remark for the transfer.
        self.remark = remark

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

        if self.idempotency_key is not None:
            result['idempotencyKey'] = self.idempotency_key

        if self.monthly_quota is not None:
            result['monthlyQuota'] = self.monthly_quota

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('idempotencyKey') is not None:
            self.idempotency_key = m.get('idempotencyKey')

        if m.get('monthlyQuota') is not None:
            self.monthly_quota = m.get('monthlyQuota')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

