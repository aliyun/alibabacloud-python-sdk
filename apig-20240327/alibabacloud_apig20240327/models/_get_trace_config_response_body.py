# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetTraceConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetTraceConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Response Data
        self.data = data
        # Error Message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Boolean	Request Result, with the following values:
        # true: Request succeeded.
        # false: Request failed.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetTraceConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetTraceConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        sample_ratio: int = None,
        service_id: str = None,
        service_port: str = None,
        trace_type: str = None,
    ):
        # Whether to Enable Tracing:
        # true: Enabled
        # false: Disabled
        self.enable = enable
        # Sampling Rate
        self.sample_ratio = sample_ratio
        # Service ID, present when the tracing type is SKYWALKING
        self.service_id = service_id
        # 服务端口，链路追踪类型为SKYWALKING时存在该参数
        self.service_port = service_port
        # Tracing Type:
        # - XTRACE
        # - SKYWALKING
        # - OPENTELEMETRY
        # - OTSKYWALKING
        self.trace_type = trace_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.sample_ratio is not None:
            result['sampleRatio'] = self.sample_ratio

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_port is not None:
            result['servicePort'] = self.service_port

        if self.trace_type is not None:
            result['traceType'] = self.trace_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('sampleRatio') is not None:
            self.sample_ratio = m.get('sampleRatio')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('servicePort') is not None:
            self.service_port = m.get('servicePort')

        if m.get('traceType') is not None:
            self.trace_type = m.get('traceType')

        return self

