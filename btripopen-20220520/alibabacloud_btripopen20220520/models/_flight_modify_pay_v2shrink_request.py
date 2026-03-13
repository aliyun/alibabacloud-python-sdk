# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightModifyPayV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        ext_params_shrink: str = None,
        isv_name: str = None,
        modify_pay_amount: int = None,
        order_id: int = None,
        out_order_id: str = None,
        out_sub_order_id: str = None,
        sub_order_id: int = None,
    ):
        self.ext_params_shrink = ext_params_shrink
        self.isv_name = isv_name
        self.modify_pay_amount = modify_pay_amount
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_sub_order_id = out_sub_order_id
        self.sub_order_id = sub_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_params_shrink is not None:
            result['ext_params'] = self.ext_params_shrink

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.modify_pay_amount is not None:
            result['modify_pay_amount'] = self.modify_pay_amount

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_sub_order_id is not None:
            result['out_sub_order_id'] = self.out_sub_order_id

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext_params') is not None:
            self.ext_params_shrink = m.get('ext_params')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('modify_pay_amount') is not None:
            self.modify_pay_amount = m.get('modify_pay_amount')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_sub_order_id') is not None:
            self.out_sub_order_id = m.get('out_sub_order_id')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        return self

