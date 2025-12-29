# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AbortChangeOrderRequest(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
        rollback: bool = None,
    ):
        # The ID of the change order.
        # 
        # This parameter is required.
        self.change_order_id = change_order_id
        self.rollback = rollback

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.rollback is not None:
            result['Rollback'] = self.rollback

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')

        return self

