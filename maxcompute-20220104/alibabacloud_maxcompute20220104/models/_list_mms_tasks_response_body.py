# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMmsTasksResponseBodyData = None,
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
            temp_model = main_models.ListMmsTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        object_list: List[main_models.ListMmsTasksResponseBodyDataObjectList] = None,
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
                temp_model = main_models.ListMmsTasksResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMmsTasksResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        db_id: int = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        dst_table_name: str = None,
        end_time: str = None,
        id: int = None,
        job_id: int = None,
        job_name: str = None,
        retried_times: int = None,
        running: bool = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        src_table_name: str = None,
        start_time: str = None,
        status: str = None,
        stopped: bool = None,
        table_id: int = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.db_id = db_id
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.dst_table_name = dst_table_name
        self.end_time = end_time
        self.id = id
        self.job_id = job_id
        self.job_name = job_name
        self.retried_times = retried_times
        self.running = running
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.src_table_name = src_table_name
        self.start_time = start_time
        self.status = status
        self.stopped = stopped
        self.table_id = table_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name

        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name

        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.id is not None:
            result['id'] = self.id

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.retried_times is not None:
            result['retriedTimes'] = self.retried_times

        if self.running is not None:
            result['running'] = self.running

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name

        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.stopped is not None:
            result['stopped'] = self.stopped

        if self.table_id is not None:
            result['tableId'] = self.table_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')

        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')

        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('retriedTimes') is not None:
            self.retried_times = m.get('retriedTimes')

        if m.get('running') is not None:
            self.running = m.get('running')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')

        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

