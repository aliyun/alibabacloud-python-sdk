# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TraceInfo(DaraModel):
    def __init__(
        self,
        duration: int = None,
        operation_name: str = None,
        service_ip: str = None,
        service_name: str = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.duration = duration
        self.operation_name = operation_name
        self.service_ip = service_ip
        self.service_name = service_name
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.operation_name is not None:
            result['operationName'] = self.operation_name

        if self.service_ip is not None:
            result['serviceIp'] = self.service_ip

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('operationName') is not None:
            self.operation_name = m.get('operationName')

        if m.get('serviceIp') is not None:
            self.service_ip = m.get('serviceIp')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

