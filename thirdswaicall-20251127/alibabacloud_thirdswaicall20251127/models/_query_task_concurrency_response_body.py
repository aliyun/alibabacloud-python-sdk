# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_thirdswaicall20251127 import models as main_models
from darabonba.model import DaraModel

class QueryTaskConcurrencyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryTaskConcurrencyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        timestamp: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp
        # Trace ID。
        self.trace_id = trace_id

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryTaskConcurrencyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self



class QueryTaskConcurrencyResponseBodyData(DaraModel):
    def __init__(
        self,
        available_concurrency: int = None,
        current_concurrency: int = None,
        max_concurrency: int = None,
    ):
        self.available_concurrency = available_concurrency
        self.current_concurrency = current_concurrency
        self.max_concurrency = max_concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_concurrency is not None:
            result['AvailableConcurrency'] = self.available_concurrency

        if self.current_concurrency is not None:
            result['CurrentConcurrency'] = self.current_concurrency

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableConcurrency') is not None:
            self.available_concurrency = m.get('AvailableConcurrency')

        if m.get('CurrentConcurrency') is not None:
            self.current_concurrency = m.get('CurrentConcurrency')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        return self

