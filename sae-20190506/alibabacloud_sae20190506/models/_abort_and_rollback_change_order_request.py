# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AbortAndRollbackChangeOrderRequest(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        # The ID of the change order.
        # 
        # This parameter is required.
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        return self

