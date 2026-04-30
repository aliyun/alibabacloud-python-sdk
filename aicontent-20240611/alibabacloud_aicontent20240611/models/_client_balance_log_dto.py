# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClientBalanceLogDTO(DaraModel):
    def __init__(
        self,
        balance_after: float = None,
        balance_before: float = None,
        change_amount: float = None,
        change_type: str = None,
        client_id: int = None,
        gmt_create: str = None,
        id: int = None,
        remark: str = None,
    ):
        self.balance_after = balance_after
        self.balance_before = balance_before
        self.change_amount = change_amount
        self.change_type = change_type
        self.client_id = client_id
        self.gmt_create = gmt_create
        self.id = id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_after is not None:
            result['balanceAfter'] = self.balance_after

        if self.balance_before is not None:
            result['balanceBefore'] = self.balance_before

        if self.change_amount is not None:
            result['changeAmount'] = self.change_amount

        if self.change_type is not None:
            result['changeType'] = self.change_type

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceAfter') is not None:
            self.balance_after = m.get('balanceAfter')

        if m.get('balanceBefore') is not None:
            self.balance_before = m.get('balanceBefore')

        if m.get('changeAmount') is not None:
            self.change_amount = m.get('changeAmount')

        if m.get('changeType') is not None:
            self.change_type = m.get('changeType')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

