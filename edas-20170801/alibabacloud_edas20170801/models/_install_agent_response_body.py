# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class InstallAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        execution_result_list: main_models.InstallAgentResponseBodyExecutionResultList = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        self.execution_result_list = execution_result_list
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.execution_result_list:
            self.execution_result_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.execution_result_list is not None:
            result['ExecutionResultList'] = self.execution_result_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExecutionResultList') is not None:
            temp_model = main_models.InstallAgentResponseBodyExecutionResultList()
            self.execution_result_list = temp_model.from_map(m.get('ExecutionResultList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InstallAgentResponseBodyExecutionResultList(DaraModel):
    def __init__(
        self,
        execution_result: List[main_models.InstallAgentResponseBodyExecutionResultListExecutionResult] = None,
    ):
        self.execution_result = execution_result

    def validate(self):
        if self.execution_result:
            for v1 in self.execution_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExecutionResult'] = []
        if self.execution_result is not None:
            for k1 in self.execution_result:
                result['ExecutionResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.execution_result = []
        if m.get('ExecutionResult') is not None:
            for k1 in m.get('ExecutionResult'):
                temp_model = main_models.InstallAgentResponseBodyExecutionResultListExecutionResult()
                self.execution_result.append(temp_model.from_map(k1))

        return self

class InstallAgentResponseBodyExecutionResultListExecutionResult(DaraModel):
    def __init__(
        self,
        finished_time: str = None,
        instance_id: str = None,
        invoke_record_status: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.finished_time = finished_time
        self.instance_id = instance_id
        self.invoke_record_status = invoke_record_status
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

