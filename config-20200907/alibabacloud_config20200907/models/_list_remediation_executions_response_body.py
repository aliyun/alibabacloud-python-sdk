# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListRemediationExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        remediation_execution_data: main_models.ListRemediationExecutionsResponseBodyRemediationExecutionData = None,
        request_id: str = None,
    ):
        # The queried remediation records.
        self.remediation_execution_data = remediation_execution_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.remediation_execution_data:
            self.remediation_execution_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation_execution_data is not None:
            result['RemediationExecutionData'] = self.remediation_execution_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationExecutionData') is not None:
            temp_model = main_models.ListRemediationExecutionsResponseBodyRemediationExecutionData()
            self.remediation_execution_data = temp_model.from_map(m.get('RemediationExecutionData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRemediationExecutionsResponseBodyRemediationExecutionData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        remediation_executions: List[main_models.ListRemediationExecutionsResponseBodyRemediationExecutionDataRemediationExecutions] = None,
    ):
        # The maximum number of entries to return for a single request.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The queried remediation records.
        self.remediation_executions = remediation_executions

    def validate(self):
        if self.remediation_executions:
            for v1 in self.remediation_executions:
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

        result['RemediationExecutions'] = []
        if self.remediation_executions is not None:
            for k1 in self.remediation_executions:
                result['RemediationExecutions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.remediation_executions = []
        if m.get('RemediationExecutions') is not None:
            for k1 in m.get('RemediationExecutions'):
                temp_model = main_models.ListRemediationExecutionsResponseBodyRemediationExecutionDataRemediationExecutions()
                self.remediation_executions.append(temp_model.from_map(k1))

        return self

class ListRemediationExecutionsResponseBodyRemediationExecutionDataRemediationExecutions(DaraModel):
    def __init__(
        self,
        execution_create_date: str = None,
        execution_invocation_id: str = None,
        execution_resource_ids: str = None,
        execution_resource_type: str = None,
        execution_status: str = None,
        execution_status_message: str = None,
    ):
        # The time when the remediation record was created.
        self.execution_create_date = execution_create_date
        # The invocation ID of the remediation record.
        self.execution_invocation_id = execution_invocation_id
        # The IDs of the resources to which the remediation belongs. Separate multiple resource IDs with commas (,).
        self.execution_resource_ids = execution_resource_ids
        # The resource type.
        self.execution_resource_type = execution_resource_type
        # The status of the remediation record. Valid values:
        # 
        # *   Success
        # *   Failed
        self.execution_status = execution_status
        # The error message returned when the remediation fails.
        self.execution_status_message = execution_status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_create_date is not None:
            result['ExecutionCreateDate'] = self.execution_create_date

        if self.execution_invocation_id is not None:
            result['ExecutionInvocationId'] = self.execution_invocation_id

        if self.execution_resource_ids is not None:
            result['ExecutionResourceIds'] = self.execution_resource_ids

        if self.execution_resource_type is not None:
            result['ExecutionResourceType'] = self.execution_resource_type

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.execution_status_message is not None:
            result['ExecutionStatusMessage'] = self.execution_status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionCreateDate') is not None:
            self.execution_create_date = m.get('ExecutionCreateDate')

        if m.get('ExecutionInvocationId') is not None:
            self.execution_invocation_id = m.get('ExecutionInvocationId')

        if m.get('ExecutionResourceIds') is not None:
            self.execution_resource_ids = m.get('ExecutionResourceIds')

        if m.get('ExecutionResourceType') is not None:
            self.execution_resource_type = m.get('ExecutionResourceType')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('ExecutionStatusMessage') is not None:
            self.execution_status_message = m.get('ExecutionStatusMessage')

        return self

