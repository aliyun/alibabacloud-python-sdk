# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnOrderCommodityCodeResponseBody(DaraModel):
    def __init__(
        self,
        order_commodity_code: str = None,
        request_id: str = None,
    ):
        # The commodity code that includes the organization unit.
        self.order_commodity_code = order_commodity_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_commodity_code is not None:
            result['OrderCommodityCode'] = self.order_commodity_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderCommodityCode') is not None:
            self.order_commodity_code = m.get('OrderCommodityCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

