# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsureRefundDetailRequest(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_user_id: str = None,
        buyer_name: str = None,
        ins_order_id: str = None,
        isv_name: str = None,
        out_apply_id: str = None,
        supplier_code: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.ins_order_id = ins_order_id
        self.isv_name = isv_name
        self.out_apply_id = out_apply_id
        self.supplier_code = supplier_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.ins_order_id is not None:
            result['ins_order_id'] = self.ins_order_id

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.out_apply_id is not None:
            result['out_apply_id'] = self.out_apply_id

        if self.supplier_code is not None:
            result['supplier_code'] = self.supplier_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('ins_order_id') is not None:
            self.ins_order_id = m.get('ins_order_id')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('out_apply_id') is not None:
            self.out_apply_id = m.get('out_apply_id')

        if m.get('supplier_code') is not None:
            self.supplier_code = m.get('supplier_code')

        return self

