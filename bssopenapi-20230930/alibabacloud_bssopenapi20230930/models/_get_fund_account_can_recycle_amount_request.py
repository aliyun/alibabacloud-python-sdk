# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFundAccountCanRecycleAmountRequest(DaraModel):
    def __init__(
        self,
        currency: str = None,
        recycle_from_fund_account_id: str = None,
    ):
        # This parameter is required.
        self.currency = currency
        self.recycle_from_fund_account_id = recycle_from_fund_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.recycle_from_fund_account_id is not None:
            result['RecycleFromFundAccountId'] = self.recycle_from_fund_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('RecycleFromFundAccountId') is not None:
            self.recycle_from_fund_account_id = m.get('RecycleFromFundAccountId')

        return self

