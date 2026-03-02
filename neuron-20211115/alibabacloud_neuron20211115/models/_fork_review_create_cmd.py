# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForkReviewCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        git_group: str = None,
        market_id: int = None,
        pbc_id: int = None,
        usage: str = None,
    ):
        self.company_id = company_id
        # This parameter is required.
        self.git_group = git_group
        self.market_id = market_id
        # This parameter is required.
        self.pbc_id = pbc_id
        # This parameter is required.
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

        if self.git_group is not None:
            result['gitGroup'] = self.git_group

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

        if m.get('gitGroup') is not None:
            self.git_group = m.get('gitGroup')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

