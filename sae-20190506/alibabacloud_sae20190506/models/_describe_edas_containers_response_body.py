# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeEdasContainersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeEdasContainersResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The components.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the list of container components of a microservices application was obtained. Valid values:
        # 
        # *   **true**: The list was obtained.
        # *   **false**: The list failed to be obtained.
        self.success = success
        # The trace ID that is used to query the details of the request.
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
                temp_model = main_models.DescribeEdasContainersResponseBodyData()
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

class DescribeEdasContainersResponseBodyData(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        edas_container_version: str = None,
    ):
        # Indicates whether the component is disabled. Valid values:
        # 
        # *   **true**: The component is disabled.
        # *   **false**: The component is not disabled.
        self.disabled = disabled
        # The version of the container, such as Ali-Tomcat, in which an application that is developed based on High-speed Service Framework (HSF) is deployed.
        self.edas_container_version = edas_container_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        return self

