# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDetailRequest(DaraModel):
    def __init__(
        self,
        change_order_num: int = None,
    ):
        # The change order number.
        # 
        # This parameter is required.
        self.change_order_num = change_order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')

        return self

