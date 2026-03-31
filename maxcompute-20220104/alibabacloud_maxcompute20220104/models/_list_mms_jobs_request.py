# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsJobsRequest(DaraModel):
    def __init__(
        self,
        sorter: main_models.ListMmsJobsRequestSorter = None,
        dst_db_name: str = None,
        dst_table_name: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        src_db_name: str = None,
        src_table_name: str = None,
        status: str = None,
        stopped: int = None,
        timer_id: int = None,
    ):
        self.sorter = sorter
        self.dst_db_name = dst_db_name
        self.dst_table_name = dst_table_name
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.src_db_name = src_db_name
        self.src_table_name = src_table_name
        self.status = status
        self.stopped = stopped
        self.timer_id = timer_id

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()

        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name

        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name

        if self.name is not None:
            result['name'] = self.name

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name

        if self.status is not None:
            result['status'] = self.status

        if self.stopped is not None:
            result['stopped'] = self.stopped

        if self.timer_id is not None:
            result['timerId'] = self.timer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = main_models.ListMmsJobsRequestSorter()
            self.sorter = temp_model.from_map(m.get('sorter'))

        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')

        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('timerId') is not None:
            self.timer_id = m.get('timerId')

        return self

class ListMmsJobsRequestSorter(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        return self

