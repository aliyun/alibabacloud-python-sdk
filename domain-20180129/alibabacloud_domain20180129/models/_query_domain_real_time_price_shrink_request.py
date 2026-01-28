# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDomainRealTimePriceShrinkRequest(DaraModel):
    def __init__(
        self,
        currency: str = None,
        domain_item_shrink: str = None,
    ):
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.domain_item_shrink = domain_item_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.domain_item_shrink is not None:
            result['DomainItem'] = self.domain_item_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DomainItem') is not None:
            self.domain_item_shrink = m.get('DomainItem')

        return self

