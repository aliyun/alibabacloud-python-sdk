# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFundAccountCanAllocateCreditAmountRequest(DaraModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        return self

