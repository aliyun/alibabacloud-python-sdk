# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInspirationAccountDetailsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        source_type: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.order_column = order_column
        self.order_type = order_type
        self.page_num = page_num
        self.page_size = page_size
        self.source_type = source_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

