# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsureOrderRefundShrinkRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        isv_name: str = None,
        out_apply_id: str = None,
        policy_no_list_shrink: str = None,
        sub_ins_order_ids_shrink: str = None,
        supplier_code: str = None,
    ):
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.isv_name = isv_name
        self.out_apply_id = out_apply_id
        self.policy_no_list_shrink = policy_no_list_shrink
        self.sub_ins_order_ids_shrink = sub_ins_order_ids_shrink
        self.supplier_code = supplier_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.out_apply_id is not None:
            result['out_apply_id'] = self.out_apply_id

        if self.policy_no_list_shrink is not None:
            result['policy_no_list'] = self.policy_no_list_shrink

        if self.sub_ins_order_ids_shrink is not None:
            result['sub_ins_order_ids'] = self.sub_ins_order_ids_shrink

        if self.supplier_code is not None:
            result['supplier_code'] = self.supplier_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('out_apply_id') is not None:
            self.out_apply_id = m.get('out_apply_id')

        if m.get('policy_no_list') is not None:
            self.policy_no_list_shrink = m.get('policy_no_list')

        if m.get('sub_ins_order_ids') is not None:
            self.sub_ins_order_ids_shrink = m.get('sub_ins_order_ids')

        if m.get('supplier_code') is not None:
            self.supplier_code = m.get('supplier_code')

        return self

