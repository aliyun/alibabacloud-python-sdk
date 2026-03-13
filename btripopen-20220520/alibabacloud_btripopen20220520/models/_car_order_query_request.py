# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CarOrderQueryRequest(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        sub_order_id: int = None,
    ):
        self.order_id = order_id
        self.sub_order_id = sub_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        return self

