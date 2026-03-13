# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelOrderChangeDetailRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        change_order_id: str = None,
        dis_order_id: str = None,
        sale_order_id: str = None,
    ):
        self.btrip_user_id = btrip_user_id
        self.change_order_id = change_order_id
        self.dis_order_id = dis_order_id
        self.sale_order_id = sale_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.change_order_id is not None:
            result['change_order_id'] = self.change_order_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.sale_order_id is not None:
            result['sale_order_id'] = self.sale_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('change_order_id') is not None:
            self.change_order_id = m.get('change_order_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('sale_order_id') is not None:
            self.sale_order_id = m.get('sale_order_id')

        return self

