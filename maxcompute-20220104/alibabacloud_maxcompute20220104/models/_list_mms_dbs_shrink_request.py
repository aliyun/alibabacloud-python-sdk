# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMmsDbsShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        sorter_shrink: str = None,
        status: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.sorter_shrink = sorter_shrink
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.sorter_shrink is not None:
            result['sorter'] = self.sorter_shrink

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sorter') is not None:
            self.sorter_shrink = m.get('sorter')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

