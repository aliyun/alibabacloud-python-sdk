# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightOrderDetailV2Request(DaraModel):
    def __init__(
        self,
        isv_name: str = None,
        order_id: int = None,
        out_order_id: str = None,
    ):
        # This parameter is required.
        self.isv_name = isv_name
        self.order_id = order_id
        self.out_order_id = out_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        return self

