# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetCreateWorkflowInstancesResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetCreateWorkflowInstancesResultResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The creation result of the workflow instance.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetCreateWorkflowInstancesResultResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetCreateWorkflowInstancesResultResponseBodyResult(DaraModel):
    def __init__(
        self,
        failure_message: str = None,
        status: str = None,
        unified_workflow_instance_ids: List[int] = None,
        workflow_instance_ids: List[int] = None,
        workflow_task_instance_ids: List[int] = None,
    ):
        # The error message. This parameter is returned only if the creation fails.
        self.failure_message = failure_message
        # The creation status. Valid values:
        # 
        # *   Creating
        # *   Created
        # *   CreateFailure
        self.status = status
        self.unified_workflow_instance_ids = unified_workflow_instance_ids
        # The workflow instance IDs. This parameter is returned only if the creation is successful.
        self.workflow_instance_ids = workflow_instance_ids
        # The list of task instance IDs corresponding to the workflow instance. This field is returned after successful creation.
        self.workflow_task_instance_ids = workflow_task_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_message is not None:
            result['FailureMessage'] = self.failure_message

        if self.status is not None:
            result['Status'] = self.status

        if self.unified_workflow_instance_ids is not None:
            result['UnifiedWorkflowInstanceIds'] = self.unified_workflow_instance_ids

        if self.workflow_instance_ids is not None:
            result['WorkflowInstanceIds'] = self.workflow_instance_ids

        if self.workflow_task_instance_ids is not None:
            result['WorkflowTaskInstanceIds'] = self.workflow_task_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureMessage') is not None:
            self.failure_message = m.get('FailureMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnifiedWorkflowInstanceIds') is not None:
            self.unified_workflow_instance_ids = m.get('UnifiedWorkflowInstanceIds')

        if m.get('WorkflowInstanceIds') is not None:
            self.workflow_instance_ids = m.get('WorkflowInstanceIds')

        if m.get('WorkflowTaskInstanceIds') is not None:
            self.workflow_task_instance_ids = m.get('WorkflowTaskInstanceIds')

        return self

