# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCompenInfosForOpRequest(DaraModel):
    def __init__(
        self,
        category: int = None,
        compen_id: str = None,
        order_id: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.compen_id = compen_id
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.compen_id is not None:
            result['compen_id'] = self.compen_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('compen_id') is not None:
            self.compen_id = m.get('compen_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

