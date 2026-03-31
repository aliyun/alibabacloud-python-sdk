# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListTaskExecutionInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_execution_invocations: List[main_models.ListTaskExecutionInvocationsResponseBodyTaskExecutionInvocations] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_execution_invocations = task_execution_invocations

    def validate(self):
        if self.task_execution_invocations:
            for v1 in self.task_execution_invocations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskExecutionInvocations'] = []
        if self.task_execution_invocations is not None:
            for k1 in self.task_execution_invocations:
                result['TaskExecutionInvocations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_execution_invocations = []
        if m.get('TaskExecutionInvocations') is not None:
            for k1 in m.get('TaskExecutionInvocations'):
                temp_model = main_models.ListTaskExecutionInvocationsResponseBodyTaskExecutionInvocations()
                self.task_execution_invocations.append(temp_model.from_map(k1))

        return self

class ListTaskExecutionInvocationsResponseBodyTaskExecutionInvocations(DaraModel):
    def __init__(
        self,
        invocation_id: str = None,
        invocation_task_execution_id: str = None,
        invocation_task_name: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.invocation_id = invocation_id
        self.invocation_task_execution_id = invocation_task_execution_id
        self.invocation_task_name = invocation_task_name
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id

        if self.invocation_task_execution_id is not None:
            result['InvocationTaskExecutionId'] = self.invocation_task_execution_id

        if self.invocation_task_name is not None:
            result['InvocationTaskName'] = self.invocation_task_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')

        if m.get('InvocationTaskExecutionId') is not None:
            self.invocation_task_execution_id = m.get('InvocationTaskExecutionId')

        if m.get('InvocationTaskName') is not None:
            self.invocation_task_name = m.get('InvocationTaskName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

