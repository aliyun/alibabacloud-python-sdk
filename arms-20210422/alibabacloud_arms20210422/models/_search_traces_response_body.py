# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class SearchTracesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trace_infos: List[main_models.SearchTracesResponseBodyTraceInfos] = None,
    ):
        self.request_id = request_id
        self.trace_infos = trace_infos

    def validate(self):
        if self.trace_infos:
            for v1 in self.trace_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k1 in self.trace_infos:
                result['TraceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k1 in m.get('TraceInfos'):
                temp_model = main_models.SearchTracesResponseBodyTraceInfos()
                self.trace_infos.append(temp_model.from_map(k1))

        return self

class SearchTracesResponseBodyTraceInfos(DaraModel):
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
            result['Duration'] = self.duration

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['TraceID'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')

        return self

