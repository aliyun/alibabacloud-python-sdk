# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsPartitionsShrinkRequest(DaraModel):
    def __init__(
        self,
        sorter: main_models.ListMmsPartitionsShrinkRequestSorter = None,
        db_id: int = None,
        db_name: str = None,
        last_ddl_time_end: str = None,
        last_ddl_time_start: str = None,
        page_num: int = None,
        page_size: int = None,
        status_shrink: str = None,
        table_id: int = None,
        table_name: str = None,
        updated: bool = None,
        value: str = None,
    ):
        self.sorter = sorter
        self.db_id = db_id
        self.db_name = db_name
        self.last_ddl_time_end = last_ddl_time_end
        self.last_ddl_time_start = last_ddl_time_start
        self.page_num = page_num
        self.page_size = page_size
        self.status_shrink = status_shrink
        self.table_id = table_id
        self.table_name = table_name
        self.updated = updated
        self.value = value

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

        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.last_ddl_time_end is not None:
            result['lastDdlTimeEnd'] = self.last_ddl_time_end

        if self.last_ddl_time_start is not None:
            result['lastDdlTimeStart'] = self.last_ddl_time_start

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status_shrink is not None:
            result['status'] = self.status_shrink

        if self.table_id is not None:
            result['tableId'] = self.table_id

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.updated is not None:
            result['updated'] = self.updated

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = main_models.ListMmsPartitionsShrinkRequestSorter()
            self.sorter = temp_model.from_map(m.get('sorter'))

        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('lastDdlTimeEnd') is not None:
            self.last_ddl_time_end = m.get('lastDdlTimeEnd')

        if m.get('lastDdlTimeStart') is not None:
            self.last_ddl_time_start = m.get('lastDdlTimeStart')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status_shrink = m.get('status')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListMmsPartitionsShrinkRequestSorter(DaraModel):
    def __init__(
        self,
        last_ddl_time: str = None,
        num_rows: str = None,
        size: str = None,
    ):
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time

        if self.num_rows is not None:
            result['numRows'] = self.num_rows

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')

        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

