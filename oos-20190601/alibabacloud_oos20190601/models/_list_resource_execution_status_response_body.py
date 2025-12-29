# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListResourceExecutionStatusResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_execution_status: List[main_models.ListResourceExecutionStatusResponseBodyResourceExecutionStatus] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The execution information of the resource.
        self.resource_execution_status = resource_execution_status

    def validate(self):
        if self.resource_execution_status:
            for v1 in self.resource_execution_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceExecutionStatus'] = []
        if self.resource_execution_status is not None:
            for k1 in self.resource_execution_status:
                result['ResourceExecutionStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_execution_status = []
        if m.get('ResourceExecutionStatus') is not None:
            for k1 in m.get('ResourceExecutionStatus'):
                temp_model = main_models.ListResourceExecutionStatusResponseBodyResourceExecutionStatus()
                self.resource_execution_status.append(temp_model.from_map(k1))

        return self

class ListResourceExecutionStatusResponseBodyResourceExecutionStatus(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        execution_time: str = None,
        outputs: str = None,
        resource_id: str = None,
        status: str = None,
    ):
        # The ID of the execution.
        self.execution_id = execution_id
        # The time when the execution started running.
        self.execution_time = execution_time
        # The output of the template.
        self.outputs = outputs
        # The ID of the resource.
        self.resource_id = resource_id
        # The status of the execution.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

