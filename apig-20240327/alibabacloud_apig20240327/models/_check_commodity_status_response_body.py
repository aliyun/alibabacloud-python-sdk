# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CheckCommodityStatusResponseBody(DaraModel):
    def __init__(
        self,
        commodities: List[main_models.CheckCommodityStatusResponseBodyCommodities] = None,
        request_id: str = None,
    ):
        # The commodity status list. Each item contains the commodity code and indicates whether the commodity capability is enabled for the current account.
        self.commodities = commodities
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.commodities:
            for v1 in self.commodities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['commodities'] = []
        if self.commodities is not None:
            for k1 in self.commodities:
                result['commodities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodities = []
        if m.get('commodities') is not None:
            for k1 in m.get('commodities'):
                temp_model = main_models.CheckCommodityStatusResponseBodyCommodities()
                self.commodities.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CheckCommodityStatusResponseBodyCommodities(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        enable: bool = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # Indicates whether the commodity capability is enabled for the current account.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

