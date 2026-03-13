# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightModifyOrderDetailV2Request(DaraModel):
    def __init__(
        self,
        isv_name: str = None,
        modify_apply_id: str = None,
        need_query_service_fee: bool = None,
        order_id: str = None,
        out_modify_apply_id: str = None,
        out_order_id: str = None,
    ):
        self.isv_name = isv_name
        self.modify_apply_id = modify_apply_id
        self.need_query_service_fee = need_query_service_fee
        self.order_id = order_id
        self.out_modify_apply_id = out_modify_apply_id
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

        if self.modify_apply_id is not None:
            result['modify_apply_id'] = self.modify_apply_id

        if self.need_query_service_fee is not None:
            result['need_query_service_fee'] = self.need_query_service_fee

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_modify_apply_id is not None:
            result['out_modify_apply_id'] = self.out_modify_apply_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('modify_apply_id') is not None:
            self.modify_apply_id = m.get('modify_apply_id')

        if m.get('need_query_service_fee') is not None:
            self.need_query_service_fee = m.get('need_query_service_fee')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_modify_apply_id') is not None:
            self.out_modify_apply_id = m.get('out_modify_apply_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        return self

