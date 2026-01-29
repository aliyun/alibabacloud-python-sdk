# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPriceEntityListRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        lang: str = None,
    ):
        # The code of the service.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

