# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPerRequestLogsInput(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        error_type: str = None,
        forward_line: int = None,
        instance_id: str = None,
        is_cold_start: bool = None,
        request_id: str = None,
        start_time: int = None,
        timestamp: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.error_type = error_type
        self.forward_line = forward_line
        self.instance_id = instance_id
        self.is_cold_start = is_cold_start
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.start_time = start_time
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.error_type is not None:
            result['errorType'] = self.error_type

        if self.forward_line is not None:
            result['forwardLine'] = self.forward_line

        if self.instance_id is not None:
            result['instanceID'] = self.instance_id

        if self.is_cold_start is not None:
            result['isColdStart'] = self.is_cold_start

        if self.request_id is not None:
            result['requestID'] = self.request_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')

        if m.get('forwardLine') is not None:
            self.forward_line = m.get('forwardLine')

        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')

        if m.get('isColdStart') is not None:
            self.is_cold_start = m.get('isColdStart')

        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

