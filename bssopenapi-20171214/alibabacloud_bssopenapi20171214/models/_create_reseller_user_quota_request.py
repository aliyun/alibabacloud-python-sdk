# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResellerUserQuotaRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        out_biz_id: str = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.currency = currency
        self.out_biz_id = out_biz_id
        # This parameter is required.
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

