# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryReimbursementOrderRequest(DaraModel):
    def __init__(
        self,
        reimb_order_no: str = None,
        sub_corp_id: str = None,
    ):
        # This parameter is required.
        self.reimb_order_no = reimb_order_no
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reimb_order_no is not None:
            result['reimb_order_no'] = self.reimb_order_no

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reimb_order_no') is not None:
            self.reimb_order_no = m.get('reimb_order_no')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        return self

