# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelOrderDetailInfoRequest(DaraModel):
    def __init__(
        self,
        btrip_order_id: str = None,
        dis_order_id: str = None,
    ):
        self.btrip_order_id = btrip_order_id
        self.dis_order_id = dis_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        return self

