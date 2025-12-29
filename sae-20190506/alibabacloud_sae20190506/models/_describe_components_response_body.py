# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeComponentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeComponentsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The details of the supported components.
        self.data = data
        # The status code. Valid values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** section of this topic.
        self.error_code = error_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the component version was obtained. Valid values:
        # 
        # *   **true**: The applications were obtained.
        # *   **false**: The applications failed to be queried.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeComponentsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class DescribeComponentsResponseBodyData(DaraModel):
    def __init__(
        self,
        component_description: str = None,
        component_key: str = None,
        expired: bool = None,
        type: str = None,
    ):
        # The description of the component.
        self.component_description = component_description
        # The component ID.
        self.component_key = component_key
        # Indicates whether the component is expired. Valid values:
        # 
        # *   **true**: The component is expired.
        # *   **false**: The component is not expired.
        self.expired = expired
        # The type of the component.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_description is not None:
            result['ComponentDescription'] = self.component_description

        if self.component_key is not None:
            result['ComponentKey'] = self.component_key

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentDescription') is not None:
            self.component_description = m.get('ComponentDescription')

        if m.get('ComponentKey') is not None:
            self.component_key = m.get('ComponentKey')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

