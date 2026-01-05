# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetWorkflowInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workflow_instance: main_models.GetWorkflowInstanceResponseBodyWorkflowInstance = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the workflow instance.
        self.workflow_instance = workflow_instance

    def validate(self):
        if self.workflow_instance:
            self.workflow_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workflow_instance is not None:
            result['WorkflowInstance'] = self.workflow_instance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkflowInstance') is not None:
            temp_model = main_models.GetWorkflowInstanceResponseBodyWorkflowInstance()
            self.workflow_instance = temp_model.from_map(m.get('WorkflowInstance'))

        return self

class GetWorkflowInstanceResponseBodyWorkflowInstance(DaraModel):
    def __init__(
        self,
        biz_date: int = None,
        create_time: int = None,
        create_user: str = None,
        env_type: str = None,
        finished_time: int = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        started_time: int = None,
        status: str = None,
        tags: List[main_models.GetWorkflowInstanceResponseBodyWorkflowInstanceTags] = None,
        type: str = None,
        unified_workflow_instance_id: int = None,
        workflow_id: int = None,
        workflow_parameters: str = None,
        workflow_task_instance_id: int = None,
    ):
        # The data timestamp.
        self.biz_date = biz_date
        # The creation time.
        self.create_time = create_time
        # The account ID of the creator.
        self.create_user = create_user
        # The environment of the workspace. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The time when the instance finished running.
        self.finished_time = finished_time
        # The ID of the workflow instance.
        self.id = id
        # The modification time.
        self.modify_time = modify_time
        # The account ID of the modifier.
        self.modify_user = modify_user
        # The name of the workflow instance.
        self.name = name
        # The account ID of the workflow owner.
        self.owner = owner
        # The workspace ID.
        self.project_id = project_id
        # The time when the instance started to run.
        self.started_time = started_time
        # The status of the workflow instance. Valid values:
        # 
        # *   NotRun: The instance is not run.
        # *   Running: The instance is running.
        # *   WaitTime: The instance is waiting for the scheduling time to arrive.
        # *   CheckingCondition: Branch conditions are being checked for the instance.
        # *   WaitResource: The instance is waiting for resources.
        # *   Failure: The instance fails to be run.
        # *   Success: The instance is successfully run.
        # *   Checking: Data quality is being checked for the instance.
        self.status = status
        # The task tag.
        self.tags = tags
        # The type of the workflow instance. Valid values:
        # 
        # *   Normal: Scheduled execution
        # *   Manual: Manually triggered node
        # *   SmokeTest: Testing
        # *   SupplementData: Data backfill
        # *   ManualWorkflow: Manually triggered workflow
        # *   TriggerWorkflow: Triggered Workflow
        self.type = type
        self.unified_workflow_instance_id = unified_workflow_instance_id
        # The ID of the workflow to which the instance belongs.
        self.workflow_id = workflow_id
        # The workflow parameters.
        self.workflow_parameters = workflow_parameters
        # The task instance ID corresponding to the workflow instance.
        self.workflow_task_instance_id = workflow_task_instance_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.unified_workflow_instance_id is not None:
            result['UnifiedWorkflowInstanceId'] = self.unified_workflow_instance_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_parameters is not None:
            result['WorkflowParameters'] = self.workflow_parameters

        if self.workflow_task_instance_id is not None:
            result['WorkflowTaskInstanceId'] = self.workflow_task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetWorkflowInstanceResponseBodyWorkflowInstanceTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UnifiedWorkflowInstanceId') is not None:
            self.unified_workflow_instance_id = m.get('UnifiedWorkflowInstanceId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowParameters') is not None:
            self.workflow_parameters = m.get('WorkflowParameters')

        if m.get('WorkflowTaskInstanceId') is not None:
            self.workflow_task_instance_id = m.get('WorkflowTaskInstanceId')

        return self

class GetWorkflowInstanceResponseBodyWorkflowInstanceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag.
        self.key = key
        # The value of a tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

