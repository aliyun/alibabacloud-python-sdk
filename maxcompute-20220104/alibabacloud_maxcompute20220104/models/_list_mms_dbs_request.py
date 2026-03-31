# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsDbsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        sorter: main_models.ListMmsDbsRequestSorter = None,
        status: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.sorter = sorter
        self.status = status

    def validate(self):
        if self.sorter:
            self.sorter.validate()

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

        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()

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
            temp_model = main_models.ListMmsDbsRequestSorter()
            self.sorter = temp_model.from_map(m.get('sorter'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListMmsDbsRequestSorter(DaraModel):
    def __init__(
        self,
        num_rows: str = None,
        size: str = None,
        update_time: str = None,
    ):
        self.num_rows = num_rows
        self.size = size
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.num_rows is not None:
            result['numRows'] = self.num_rows

        if self.size is not None:
            result['size'] = self.size

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

