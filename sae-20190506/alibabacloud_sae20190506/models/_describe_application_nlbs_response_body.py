# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationNlbsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationNlbsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned data.
        self.data = data
        # The status code. Value values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** section in this topic.
        self.error_code = error_code
        # The message returned. Valid values:If the request was successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the NLB instance was successfully associated with the application. Valid values:
        # 
        # *   **true**: The application was associated.
        # *   **false**: The application failed to be associated.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeApplicationNlbsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeApplicationNlbsResponseBodyData(DaraModel):
    def __init__(
        self,
        instances: Dict[str, main_models.DataInstancesValue] = None,
    ):
        # The details of the instance.
        self.instances = instances

    def validate(self):
        if self.instances:
            for v1 in self.instances.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = {}
        if self.instances is not None:
            for k1, v1 in self.instances.items():
                result['Instances'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = {}
        if m.get('Instances') is not None:
            for k1, v1 in m.get('Instances').items():
                temp_model = main_models.DataInstancesValue()
                self.instances[k1] = temp_model.from_map(v1)

        return self

