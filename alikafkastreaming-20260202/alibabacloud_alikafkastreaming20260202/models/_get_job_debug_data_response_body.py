# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class GetJobDebugDataResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetJobDebugDataResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetJobDebugDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetJobDebugDataResponseBodyData(DaraModel):
    def __init__(
        self,
        data_rows: List[main_models.GetJobDebugDataResponseBodyDataDataRows] = None,
        debug_field: str = None,
        has_more: bool = None,
        limit: str = None,
        next_cursor: str = None,
    ):
        self.data_rows = data_rows
        self.debug_field = debug_field
        self.has_more = has_more
        self.limit = limit
        self.next_cursor = next_cursor

    def validate(self):
        if self.data_rows:
            for v1 in self.data_rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataRows'] = []
        if self.data_rows is not None:
            for k1 in self.data_rows:
                result['DataRows'].append(k1.to_map() if k1 else None)

        if self.debug_field is not None:
            result['DebugField'] = self.debug_field

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_rows = []
        if m.get('DataRows') is not None:
            for k1 in m.get('DataRows'):
                temp_model = main_models.GetJobDebugDataResponseBodyDataDataRows()
                self.data_rows.append(temp_model.from_map(k1))

        if m.get('DebugField') is not None:
            self.debug_field = m.get('DebugField')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')

        return self

class GetJobDebugDataResponseBodyDataDataRows(DaraModel):
    def __init__(
        self,
        flink_instance_id: str = None,
        job_name: str = None,
        offset: int = None,
        partition: int = None,
        processed_value: str = None,
        timestamp: int = None,
        uuid: str = None,
    ):
        self.flink_instance_id = flink_instance_id
        self.job_name = job_name
        self.offset = offset
        self.partition = partition
        self.processed_value = processed_value
        self.timestamp = timestamp
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flink_instance_id is not None:
            result['FlinkInstanceId'] = self.flink_instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.partition is not None:
            result['Partition'] = self.partition

        if self.processed_value is not None:
            result['ProcessedValue'] = self.processed_value

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlinkInstanceId') is not None:
            self.flink_instance_id = m.get('FlinkInstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('ProcessedValue') is not None:
            self.processed_value = m.get('ProcessedValue')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

