# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundDetailListRequest(DaraModel):
    def __init__(
        self,
        order_num: int = None,
        page_index: int = None,
        page_size: int = None,
        refund_create_begin_time: int = None,
        refund_create_end_time: int = None,
    ):
        # The order number.
        self.order_num = order_num
        # The page index.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size
        # The start time for refund order creation. The value is a UTC timestamp.
        # 
        # This parameter is required.
        self.refund_create_begin_time = refund_create_begin_time
        # The end time for refund order creation. The value is a UTC timestamp.
        # 
        # This parameter is required.
        self.refund_create_end_time = refund_create_end_time

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

        if self.refund_create_begin_time is not None:
            result['refund_create_begin_time'] = self.refund_create_begin_time

        if self.refund_create_end_time is not None:
            result['refund_create_end_time'] = self.refund_create_end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('refund_create_begin_time') is not None:
            self.refund_create_begin_time = m.get('refund_create_begin_time')

        if m.get('refund_create_end_time') is not None:
            self.refund_create_end_time = m.get('refund_create_end_time')

        return self

