# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateBalanceTransactionRequest(DaraModel):
    def __init__(
        self,
        amount: float = None,
        remark: str = None,
        type: str = None,
    ):
        self.amount = amount
        self.remark = remark
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

        if self.remark is not None:
            result['remark'] = self.remark

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

