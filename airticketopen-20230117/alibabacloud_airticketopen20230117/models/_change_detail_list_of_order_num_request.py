# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDetailListOfOrderNumRequest(DaraModel):
    def __init__(
        self,
        order_num: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # The order number.
        # 
        # This parameter is required.
        self.order_num = order_num
        # The page index.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.page_index is not None:
            result['page_index'] = self.page_index

        if self.page_size is not None:
            result['page_size'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        return self

