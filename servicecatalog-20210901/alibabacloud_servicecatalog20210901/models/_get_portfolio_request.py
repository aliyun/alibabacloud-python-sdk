# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPortfolioRequest(DaraModel):
    def __init__(
        self,
        portfolio_id: str = None,
    ):
        # The ID of the product portfolio.
        # 
        # This parameter is required.
        self.portfolio_id = portfolio_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        return self

