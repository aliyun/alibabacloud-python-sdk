# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnsSaleControlAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        custom_account: str = None,
        order_type: str = None,
    ):
        # This parameter is required.
        self.commodity_code = commodity_code
        self.custom_account = custom_account
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.custom_account is not None:
            result['CustomAccount'] = self.custom_account

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomAccount') is not None:
            self.custom_account = m.get('CustomAccount')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

