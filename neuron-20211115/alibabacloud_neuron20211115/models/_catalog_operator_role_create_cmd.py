# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CatalogOperatorRoleCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        market_id: int = None,
        market_type: str = None,
    ):
        # This parameter is required.
        self.company_id = company_id
        # This parameter is required.
        self.market_id = market_id
        # This parameter is required.
        self.market_type = market_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.market_type is not None:
            result['marketType'] = self.market_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('marketType') is not None:
            self.market_type = m.get('marketType')

        return self

