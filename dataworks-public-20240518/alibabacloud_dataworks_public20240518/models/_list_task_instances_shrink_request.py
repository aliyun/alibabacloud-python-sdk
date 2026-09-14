# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTaskInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        filter: str = None,
        id: int = None,
        ids_shrink: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_env: str = None,
        project_id: int = None,
        runtime_resource: str = None,
        sort_by: str = None,
        status: str = None,
        task_id: int = None,
        task_ids_shrink: str = None,
        task_name: str = None,
        task_type: str = None,
        trigger_recurrence: str = None,
        trigger_type: str = None,
        unified_workflow_instance_id: int = None,
        workflow_id: int = None,
        workflow_instance_id: int = None,
        workflow_instance_type: str = None,
    ):
        # The business date. This is typically 00:00:00 of the day before the scheduled time of the periodic instance. The value is a millisecond-level timestamp, such as 1743350400000.
        # 
        # This parameter is required.
        self.bizdate = bizdate
        # The filter. The value is in JSON format. Multiple filter conditions are combined with AND logic. Currently supported fields: `startedTimeStart, startedTimeEnd, finishedTimeStart, finishedTimeEnd, createTimeStart, createTimeEnd`
        self.filter = filter
        # The instance ID. If an instance has been rerun, specifying this parameter returns the historical information including reruns. You can use RunNumber to distinguish each historical record.
        self.id = id
        # The list of instance IDs. You can use this parameter to query multiple instances in a batch.
        self.ids_shrink = ids_shrink
        # The account ID of the node owner.
        self.owner = owner
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 500.
        self.page_size = page_size
        # The project environment. Valid values:
        # - Prod: production.
        # - Dev: development.
        self.project_env = project_env
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The schedule resource information. Specify the identifier of the schedule resource group.
        self.runtime_resource = runtime_resource
        # The sort field. Supports fields such as scheduled time and start time. The format is "sort field + sort order (Desc/Asc)". Asc can be omitted. Valid values:
        # 
        # - `TriggerTime (Desc/Asc)`
        # 
        # - `StartedTime (Desc/Asc)`
        # 
        # - `FinishedTime (Desc/Asc)`
        # 
        # - `CreateTime (Desc/Asc)`
        # 
        # - `Id (Desc/Asc)`
        # 
        #   Default value: `Id Desc`
        self.sort_by = sort_by
        # The status of the instance. Valid values:
        # - `NotRun`: not run.
        # - `Running`: running.
        # - `Failure`: failed.
        # - `Success`: succeeded.
        # - `WaitTime`: waiting for the scheduled time.
        # - `WaitResource`: waiting for resources.
        self.status = status
        # The ID of the corresponding node.
        self.task_id = task_id
        # The list of node IDs. You can use this parameter to query instances of multiple nodes in a batch.
        self.task_ids_shrink = task_ids_shrink
        # The name of the corresponding node. Fuzzy match is supported.
        self.task_name = task_name
        # The node type. For the TaskType values of each node, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.task_type = task_type
        # The run mode at the time of triggering. This parameter takes effect only when TriggerType is set to Scheduler. Valid values:
        # - Pause: paused.
        # - Skip: dry run.
        # - Normal: normal run.
        self.trigger_recurrence = trigger_recurrence
        # The trigger type. Valid values:
        # - Scheduler: triggered by periodic scheduling.
        # - Manual: manually triggered.
        self.trigger_type = trigger_type
        # The unified workflow instance ID. All instances within the same business date under a single trigger share the same value for this field.
        self.unified_workflow_instance_id = unified_workflow_instance_id
        # The ID of the workflow to which the instance belongs.
        self.workflow_id = workflow_id
        # The ID of the workflow instance to which the instance belongs.
        self.workflow_instance_id = workflow_instance_id
        # The type of the workflow instance to which the instance belongs. Valid values:
        # - SmokeTest: test.
        # - Manual: manual node.
        # - SupplementData: data backfill.
        # - ManualWorkflow: manual workflow.
        # - Normal: periodic scheduling.
        # - TriggerWorkflow: trigger-based workflow.
        self.workflow_instance_type = workflow_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.id is not None:
            result['Id'] = self.id

        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_ids_shrink is not None:
            result['TaskIds'] = self.task_ids_shrink

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.trigger_recurrence is not None:
            result['TriggerRecurrence'] = self.trigger_recurrence

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.unified_workflow_instance_id is not None:
            result['UnifiedWorkflowInstanceId'] = self.unified_workflow_instance_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        if self.workflow_instance_type is not None:
            result['WorkflowInstanceType'] = self.workflow_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            self.runtime_resource = m.get('RuntimeResource')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskIds') is not None:
            self.task_ids_shrink = m.get('TaskIds')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TriggerRecurrence') is not None:
            self.trigger_recurrence = m.get('TriggerRecurrence')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('UnifiedWorkflowInstanceId') is not None:
            self.unified_workflow_instance_id = m.get('UnifiedWorkflowInstanceId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        if m.get('WorkflowInstanceType') is not None:
            self.workflow_instance_type = m.get('WorkflowInstanceType')

        return self

