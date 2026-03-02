# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcInvokeReviewCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        invoke_pbc_id: int = None,
        market_id: int = None,
        pbc_id: int = None,
        usage: str = None,
    ):
        self.company_id = company_id
        self.invoke_pbc_id = invoke_pbc_id
        self.market_id = market_id
        self.pbc_id = pbc_id
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.invoke_pbc_id is not None:
            result['invokePbcId'] = self.invoke_pbc_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('invokePbcId') is not None:
            self.invoke_pbc_id = m.get('invokePbcId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

