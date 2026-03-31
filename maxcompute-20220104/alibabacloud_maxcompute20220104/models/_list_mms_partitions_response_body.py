# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsPartitionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMmsPartitionsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListMmsPartitionsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsPartitionsResponseBodyData(DaraModel):
    def __init__(
        self,
        object_list: List[main_models.ListMmsPartitionsResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for v1 in self.object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['objectList'] = []
        if self.object_list is not None:
            for k1 in self.object_list:
                result['objectList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k1 in m.get('objectList'):
                temp_model = main_models.ListMmsPartitionsResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMmsPartitionsResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        dst_project_name: str = None,
        dst_schema_name: str = None,
        dst_table_name: str = None,
        dst_value: str = None,
        id: int = None,
        last_ddl_time: str = None,
        num_rows: int = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        table_id: int = None,
        table_name: str = None,
        updated: bool = None,
        value: str = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.dst_project_name = dst_project_name
        self.dst_schema_name = dst_schema_name
        self.dst_table_name = dst_table_name
        self.dst_value = dst_value
        self.id = id
        # lastDdlTime
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.table_id = table_id
        self.table_name = table_name
        self.updated = updated
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.dst_project_name is not None:
            result['dstProjectName'] = self.dst_project_name

        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name

        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name

        if self.dst_value is not None:
            result['dstValue'] = self.dst_value

        if self.id is not None:
            result['id'] = self.id

        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time

        if self.num_rows is not None:
            result['numRows'] = self.num_rows

        if self.size is not None:
            result['size'] = self.size

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.status is not None:
            result['status'] = self.status

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
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dstProjectName') is not None:
            self.dst_project_name = m.get('dstProjectName')

        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')

        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')

        if m.get('dstValue') is not None:
            self.dst_value = m.get('dstValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')

        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

