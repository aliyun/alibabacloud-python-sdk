# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribeQuickSaleConfigResponseBody(DaraModel):
    def __init__(
        self,
        commodity: str = None,
        items: Dict[str, Any] = None,
        request_id: str = None,
    ):
        # The product code. Valid values:
        # 
        # *   rds: The instance is a subscription instance.
        # *   bards: The instance is a pay-as-you-go instance.
        self.commodity = commodity
        # The configuration details of the product.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity is not None:
            result['Commodity'] = self.commodity

        if self.items is not None:
            result['Items'] = self.items

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

