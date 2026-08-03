# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelOrderRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        order_no: str = None,
        tracer_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.order_no = order_no
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.order_no is not None:
            result['OrderNo'] = self.order_no

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

