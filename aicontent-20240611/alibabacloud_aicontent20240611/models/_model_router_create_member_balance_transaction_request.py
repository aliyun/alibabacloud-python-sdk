# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateMemberBalanceTransactionRequest(DaraModel):
    def __init__(
        self,
        amount: float = None,
        balance_type: str = None,
        idempotency_key: str = None,
        remark: str = None,
        type: str = None,
    ):
        # The transaction amount.
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
        # The remark for the transaction.
        self.remark = remark
        # The transaction type. Valid values: recharge, deduct, and transfer.
        self.type = type

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

        if self.remark is not None:
            result['remark'] = self.remark

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('idempotencyKey') is not None:
            self.idempotency_key = m.get('idempotencyKey')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

