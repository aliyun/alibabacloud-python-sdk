# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSpecificationsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeInstanceSpecificationsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request is successful.
        # 
        # - **3xx**: The request is redirected.
        # 
        # - **4xx**: The request is invalid.
        # 
        # - **5xx**: A server error occurs.
        self.code = code
        # The instance specifications.
        self.data = data
        # The error code.
        # 
        # - The **ErrorCode** parameter is not returned if the request is successful.
        # 
        # - The **ErrorCode** parameter is returned if the request fails. For more information, see the **Error codes** section of this topic.
        self.error_code = error_code
        # The returned message.
        # 
        # - If the request is successful, **success** is returned.
        # 
        # - If the request fails, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the instance specifications are obtained. Valid values:
        # 
        # - **true**: The instance specifications are obtained.
        # 
        # - **false**: The instance specifications fail to be obtained.
        self.success = success
        # The trace ID that is used to query the details of a request.
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
                temp_model = main_models.DescribeInstanceSpecificationsResponseBodyData()
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

class DescribeInstanceSpecificationsResponseBodyData(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        enable: bool = None,
        id: int = None,
        memory: int = None,
        spec_info: str = None,
        version: int = None,
    ):
        # The CPU specification. Unit: millicores.
        self.cpu = cpu
        # Indicates whether the instance specification is available. Valid values:
        # 
        # - **true**: available
        # 
        # - **false**: unavailable
        self.enable = enable
        # The ID of the instance specification.
        self.id = id
        # The memory specification. Unit: MB.
        self.memory = memory
        # The name of the instance specification.
        self.spec_info = spec_info
        # The version of the instance specification.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.id is not None:
            result['Id'] = self.id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.spec_info is not None:
            result['SpecInfo'] = self.spec_info

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SpecInfo') is not None:
            self.spec_info = m.get('SpecInfo')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

