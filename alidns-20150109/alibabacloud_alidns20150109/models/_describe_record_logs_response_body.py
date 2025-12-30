# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordLogsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        record_logs: main_models.DescribeRecordLogsResponseBodyRecordLogs = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The operation logs.
        self.record_logs = record_logs
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.record_logs:
            self.record_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_logs is not None:
            result['RecordLogs'] = self.record_logs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordLogs') is not None:
            temp_model = main_models.DescribeRecordLogsResponseBodyRecordLogs()
            self.record_logs = temp_model.from_map(m.get('RecordLogs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRecordLogsResponseBodyRecordLogs(DaraModel):
    def __init__(
        self,
        record_log: List[main_models.DescribeRecordLogsResponseBodyRecordLogsRecordLog] = None,
    ):
        self.record_log = record_log

    def validate(self):
        if self.record_log:
            for v1 in self.record_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordLog'] = []
        if self.record_log is not None:
            for k1 in self.record_log:
                result['RecordLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_log = []
        if m.get('RecordLog') is not None:
            for k1 in m.get('RecordLog'):
                temp_model = main_models.DescribeRecordLogsResponseBodyRecordLogsRecordLog()
                self.record_log.append(temp_model.from_map(k1))

        return self

class DescribeRecordLogsResponseBodyRecordLogsRecordLog(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_time: str = None,
        action_timestamp: int = None,
        client_ip: str = None,
        message: str = None,
    ):
        # The operation that you performed.
        self.action = action
        # The time when you performed the operation.
        self.action_time = action_time
        # The time when you performed the operation. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.action_timestamp = action_timestamp
        # The IP address of the operator.
        self.client_ip = client_ip
        # The operation message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_time is not None:
            result['ActionTime'] = self.action_time

        if self.action_timestamp is not None:
            result['ActionTimestamp'] = self.action_timestamp

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')

        if m.get('ActionTimestamp') is not None:
            self.action_timestamp = m.get('ActionTimestamp')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

