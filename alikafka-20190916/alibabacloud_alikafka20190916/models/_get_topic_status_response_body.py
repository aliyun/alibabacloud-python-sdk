# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetTopicStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        topic_status: main_models.GetTopicStatusResponseBodyTopicStatus = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The status information about messages in the topic.
        self.topic_status = topic_status

    def validate(self):
        if self.topic_status:
            self.topic_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_status is not None:
            result['TopicStatus'] = self.topic_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicStatus') is not None:
            temp_model = main_models.GetTopicStatusResponseBodyTopicStatus()
            self.topic_status = temp_model.from_map(m.get('TopicStatus'))

        return self

class GetTopicStatusResponseBodyTopicStatus(DaraModel):
    def __init__(
        self,
        last_time_stamp: int = None,
        offset_table: main_models.GetTopicStatusResponseBodyTopicStatusOffsetTable = None,
        total_count: int = None,
    ):
        # The time when the last consumed message was generated.
        self.last_time_stamp = last_time_stamp
        self.offset_table = offset_table
        # The number of messages in the topic.
        self.total_count = total_count

    def validate(self):
        if self.offset_table:
            self.offset_table.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp

        if self.offset_table is not None:
            result['OffsetTable'] = self.offset_table.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')

        if m.get('OffsetTable') is not None:
            temp_model = main_models.GetTopicStatusResponseBodyTopicStatusOffsetTable()
            self.offset_table = temp_model.from_map(m.get('OffsetTable'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetTopicStatusResponseBodyTopicStatusOffsetTable(DaraModel):
    def __init__(
        self,
        offset_table: List[main_models.GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable] = None,
    ):
        self.offset_table = offset_table

    def validate(self):
        if self.offset_table:
            for v1 in self.offset_table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OffsetTable'] = []
        if self.offset_table is not None:
            for k1 in self.offset_table:
                result['OffsetTable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.offset_table = []
        if m.get('OffsetTable') is not None:
            for k1 in m.get('OffsetTable'):
                temp_model = main_models.GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable()
                self.offset_table.append(temp_model.from_map(k1))

        return self

class GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable(DaraModel):
    def __init__(
        self,
        last_update_timestamp: int = None,
        max_offset: int = None,
        min_offset: int = None,
        partition: int = None,
        topic: str = None,
    ):
        self.last_update_timestamp = last_update_timestamp
        self.max_offset = max_offset
        self.min_offset = min_offset
        self.partition = partition
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_update_timestamp is not None:
            result['LastUpdateTimestamp'] = self.last_update_timestamp

        if self.max_offset is not None:
            result['MaxOffset'] = self.max_offset

        if self.min_offset is not None:
            result['MinOffset'] = self.min_offset

        if self.partition is not None:
            result['Partition'] = self.partition

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUpdateTimestamp') is not None:
            self.last_update_timestamp = m.get('LastUpdateTimestamp')

        if m.get('MaxOffset') is not None:
            self.max_offset = m.get('MaxOffset')

        if m.get('MinOffset') is not None:
            self.min_offset = m.get('MinOffset')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

