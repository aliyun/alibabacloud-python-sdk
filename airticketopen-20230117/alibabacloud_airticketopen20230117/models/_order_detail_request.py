# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OrderDetailRequest(DaraModel):
    def __init__(
        self,
        order_num: int = None,
        out_order_num: str = None,
    ):
        # The order number.
        self.order_num = order_num
        # The external order number.
        self.out_order_num = out_order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')

        return self

