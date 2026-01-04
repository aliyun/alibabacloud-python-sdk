# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileSystemShrinkRequest(DaraModel):
    def __init__(
        self,
        order_details_shrink: str = None,
    ):
        # The information about the orders.
        # 
        # This parameter is required.
        self.order_details_shrink = order_details_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_details_shrink is not None:
            result['OrderDetails'] = self.order_details_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderDetails') is not None:
            self.order_details_shrink = m.get('OrderDetails')

        return self

