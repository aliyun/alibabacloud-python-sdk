# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePushMeteringDataRequest(DaraModel):
    def __init__(
        self,
        push_order_biz_id: str = None,
    ):
        # This parameter is required.
        self.push_order_biz_id = push_order_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_order_biz_id is not None:
            result['PushOrderBizId'] = self.push_order_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushOrderBizId') is not None:
            self.push_order_biz_id = m.get('PushOrderBizId')

        return self

