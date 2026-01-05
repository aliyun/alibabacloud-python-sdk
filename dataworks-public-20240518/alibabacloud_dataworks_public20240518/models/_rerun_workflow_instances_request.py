# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class RerunWorkflowInstancesRequest(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        end_trigger_time: int = None,
        env_type: str = None,
        filter: main_models.RerunWorkflowInstancesRequestFilter = None,
        ids: List[int] = None,
        name: str = None,
        project_id: int = None,
        start_trigger_time: int = None,
        status: str = None,
        type: str = None,
        workflow_id: int = None,
    ):
        # The business date used for matching manual workflow instances.
        self.bizdate = bizdate
        # The end trigger time of the manual workflow instance used for matching. This parameter must be used together with the StartTriggerTime.
        self.end_trigger_time = end_trigger_time
        # The environment of the workspace. Valid values:
        # 
        # Prod Dev
        self.env_type = env_type
        # The match conditions for internal instances of manual workflow instances.
        self.filter = filter
        # The instance IDs used for matching manual workflow instances.
        self.ids = ids
        # The manual workflow name, used for fuzzy matching.
        self.name = name
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The start trigger time (creation time) of the manual workflow instance used for matching. This parameter must be used together with EndTriggerTime.
        self.start_trigger_time = start_trigger_time
        # The status used for matching manual workflow instances.
        # 
        # Valid values:
        # 
        # *   Success
        # *   Failure
        self.status = status
        # The type of the workflow instance. Valid values:
        # 
        # ManualWorkflow.
        # 
        # This parameter is required.
        self.type = type
        # The workflow ID.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.end_trigger_time is not None:
            result['EndTriggerTime'] = self.end_trigger_time

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.start_trigger_time is not None:
            result['StartTriggerTime'] = self.start_trigger_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('EndTriggerTime') is not None:
            self.end_trigger_time = m.get('EndTriggerTime')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Filter') is not None:
            temp_model = main_models.RerunWorkflowInstancesRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartTriggerTime') is not None:
            self.start_trigger_time = m.get('StartTriggerTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class RerunWorkflowInstancesRequestFilter(DaraModel):
    def __init__(
        self,
        rerun_downstream_enabled: bool = None,
        task_ids: List[int] = None,
        task_instance_statuses: List[str] = None,
        task_name: str = None,
        task_types: List[str] = None,
    ):
        # Specifies whether to rerun the matched instances and all downstream instances.
        self.rerun_downstream_enabled = rerun_downstream_enabled
        # The internal task IDs used for matching manual workflow instances.
        self.task_ids = task_ids
        # The statuses of internal tasks used for matching manual workflow instances.
        self.task_instance_statuses = task_instance_statuses
        # The internal task name used for matching the manual workflow instance.
        self.task_name = task_name
        # Match internal tasks within the manual workflow by type.
        self.task_types = task_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rerun_downstream_enabled is not None:
            result['RerunDownstreamEnabled'] = self.rerun_downstream_enabled

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.task_instance_statuses is not None:
            result['TaskInstanceStatuses'] = self.task_instance_statuses

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_types is not None:
            result['TaskTypes'] = self.task_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RerunDownstreamEnabled') is not None:
            self.rerun_downstream_enabled = m.get('RerunDownstreamEnabled')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('TaskInstanceStatuses') is not None:
            self.task_instance_statuses = m.get('TaskInstanceStatuses')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')

        return self

