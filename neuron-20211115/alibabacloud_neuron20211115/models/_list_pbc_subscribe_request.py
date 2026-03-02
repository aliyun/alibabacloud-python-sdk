# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPbcSubscribeRequest(DaraModel):
    def __init__(
        self,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.order_direction is not None:
            result['order_direction'] = self.order_direction

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        return self

