# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_thirdswaicall20251127 import models as main_models
from darabonba.model import DaraModel

class CreateCallOutboundInstantResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCallOutboundInstantResponseBodyData = None,
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
            temp_model = main_models.CreateCallOutboundInstantResponseBodyData()
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



class CreateCallOutboundInstantResponseBodyData(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        call_status: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.call_id = call_id
        self.call_status = call_status
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

