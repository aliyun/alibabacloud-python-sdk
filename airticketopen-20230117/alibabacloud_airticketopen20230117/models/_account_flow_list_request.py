# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccountFlowListRequest(DaraModel):
    def __init__(
        self,
        day_num: int = None,
        page_index: int = None,
        page_size: int = None,
        utc_begin_time: int = None,
    ):
        # The number of days to search. Maximum value: 30. Valid values: 0 to 30.
        # 
        # This parameter is required.
        self.day_num = day_num
        # The page index.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size
        # The start search timestamp, effective to the day. Specify a 13-digit UTC timestamp.
        # 
        # This parameter is required.
        self.utc_begin_time = utc_begin_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_num is not None:
            result['day_num'] = self.day_num

        if self.page_index is not None:
            result['page_index'] = self.page_index

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.utc_begin_time is not None:
            result['utc_begin_time'] = self.utc_begin_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('day_num') is not None:
            self.day_num = m.get('day_num')

        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('utc_begin_time') is not None:
            self.utc_begin_time = m.get('utc_begin_time')

        return self

