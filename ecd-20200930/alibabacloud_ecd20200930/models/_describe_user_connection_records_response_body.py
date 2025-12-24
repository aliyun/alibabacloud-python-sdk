# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeUserConnectionRecordsResponseBody(DaraModel):
    def __init__(
        self,
        connection_records: List[main_models.DescribeUserConnectionRecordsResponseBodyConnectionRecords] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The connection records.
        self.connection_records = connection_records
        # The token that is used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.connection_records:
            for v1 in self.connection_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnectionRecords'] = []
        if self.connection_records is not None:
            for k1 in self.connection_records:
                result['ConnectionRecords'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_records = []
        if m.get('ConnectionRecords') is not None:
            for k1 in m.get('ConnectionRecords'):
                temp_model = main_models.DescribeUserConnectionRecordsResponseBodyConnectionRecords()
                self.connection_records.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserConnectionRecordsResponseBodyConnectionRecords(DaraModel):
    def __init__(
        self,
        connect_duration: str = None,
        connect_end_time: str = None,
        connect_start_time: str = None,
        connection_record_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
    ):
        # The connection duration. Unit: milliseconds.
        self.connect_duration = connect_duration
        # The time when the end user disconnected from the cloud computer.
        self.connect_end_time = connect_end_time
        # The time when the end user connected to the cloud computer.
        self.connect_start_time = connect_start_time
        # The ID of the connection record.
        self.connection_record_id = connection_record_id
        # The ID of the cloud computer to which the end user connected.
        self.desktop_id = desktop_id
        # The name of the cloud computer to which the end user connected.
        self.desktop_name = desktop_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration

        if self.connect_end_time is not None:
            result['ConnectEndTime'] = self.connect_end_time

        if self.connect_start_time is not None:
            result['ConnectStartTime'] = self.connect_start_time

        if self.connection_record_id is not None:
            result['ConnectionRecordId'] = self.connection_record_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')

        if m.get('ConnectEndTime') is not None:
            self.connect_end_time = m.get('ConnectEndTime')

        if m.get('ConnectStartTime') is not None:
            self.connect_start_time = m.get('ConnectStartTime')

        if m.get('ConnectionRecordId') is not None:
            self.connection_record_id = m.get('ConnectionRecordId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        return self

