# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetStackResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_info: List[main_models.GetStackResponseBodyStackInfo] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The method stack details.
        self.stack_info = stack_info

    def validate(self):
        if self.stack_info:
            for v1 in self.stack_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StackInfo'] = []
        if self.stack_info is not None:
            for k1 in self.stack_info:
                result['StackInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stack_info = []
        if m.get('StackInfo') is not None:
            for k1 in m.get('StackInfo'):
                temp_model = main_models.GetStackResponseBodyStackInfo()
                self.stack_info.append(temp_model.from_map(k1))

        return self

class GetStackResponseBodyStackInfo(DaraModel):
    def __init__(
        self,
        api: str = None,
        call_count: str = None,
        duration: int = None,
        exception: str = None,
        ext_info: main_models.GetStackResponseBodyStackInfoExtInfo = None,
        line: str = None,
        rpc_id: str = None,
        service_name: str = None,
        start_time: int = None,
    ):
        # The name of the operation.
        self.api = api
        # The number of times the method is called.
        self.call_count = call_count
        # The duration. Unit: milliseconds.
        self.duration = duration
        # The error message.
        self.exception = exception
        # The information about the array object.
        self.ext_info = ext_info
        # The number of rows in the method stack information.
        self.line = line
        # The ID of the RPC mode.
        self.rpc_id = rpc_id
        # The name of the service.
        self.service_name = service_name
        # The start time of the call method.
        self.start_time = start_time

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['Api'] = self.api

        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.exception is not None:
            result['Exception'] = self.exception

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()

        if self.line is not None:
            result['Line'] = self.line

        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Exception') is not None:
            self.exception = m.get('Exception')

        if m.get('ExtInfo') is not None:
            temp_model = main_models.GetStackResponseBodyStackInfoExtInfo()
            self.ext_info = temp_model.from_map(m.get('ExtInfo'))

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetStackResponseBodyStackInfoExtInfo(DaraModel):
    def __init__(
        self,
        info: str = None,
        type: str = None,
    ):
        # The content of the custom parameter.
        self.info = info
        # The type of the custom parameter.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

