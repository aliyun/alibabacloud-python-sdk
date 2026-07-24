# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundDetailRequest(DaraModel):
    def __init__(
        self,
        refund_order_num: int = None,
    ):
        # The refund order number.
        # 
        # This parameter is required.
        self.refund_order_num = refund_order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')

        return self

