# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTaskInstancesRequest(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        filter: str = None,
        id: int = None,
        ids: List[int] = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_env: str = None,
        project_id: int = None,
        runtime_resource: str = None,
        sort_by: str = None,
        status: str = None,
        task_id: int = None,
        task_ids: List[int] = None,
        task_name: str = None,
        task_type: str = None,
        trigger_recurrence: str = None,
        trigger_type: str = None,
        unified_workflow_instance_id: int = None,
        workflow_id: int = None,
        workflow_instance_id: int = None,
        workflow_instance_type: str = None,
    ):
        # The business date. Typically, this is 00:00:00 of the day before the scheduled time of the scheduled instance, in the format of a millisecond-level timestamp, such as 1743350400000.
        # 
        # This parameter is required.
        self.bizdate = bizdate
        # The filter conditions. The value must be in JSON format. Multiple filter conditions are connected by the logical AND operator. Supported fields: `startedTimeStart`, `startedTimeEnd`, `finishedTimeStart`, `finishedTimeEnd`, `createTimeStart`, and `createTimeEnd`.
        self.filter = filter
        # The task instance ID. Task instances may be rerun. If you specify this parameter, the response includes historical information about reruns. Each piece of historical information is distinguished by RunNumber.
        self.id = id
        # The list of task instance IDs. You can use this parameter to query multiple task instances in batches based on task instance IDs.
        self.ids = ids
        # The account ID of the task owner.
        self.owner = owner
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 500.
        self.page_size = page_size
        # The project environment.
        # - Prod: Production.
        # - Dev: Development.
        self.project_env = project_env
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The resource group information. Specify the identifier of the scheduling resource group.
        self.runtime_resource = runtime_resource
        # The sort field. Fields such as scheduled time and start time are supported. The format is "Sort field + Sort order (Desc/Asc)" (Asc can be omitted). The valid values for the sort field are as follows:
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
        #   Default value: `Id Desc`.
        self.sort_by = sort_by
        # The status of the task instance. Valid values:
        # - `NotRun`: Not run.
        # - `Running`: Running.
        # - `Failure`: Failed.
        # - `Success`: Successful.
        # - `WaitTime`: Waiting for scheduled time.
        # - `WaitResource`: Waiting for resources.
        self.status = status
        # The ID of the task.
        self.task_id = task_id
        # The list of task IDs. You can use this parameter to query task instances in batches based on task IDs.
        self.task_ids = task_ids
        # The name of the task. Fuzzy match is supported.
        self.task_name = task_name
        # The task type. For the valid values of TaskType for different nodes, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.task_type = task_type
        # The running mode upon triggering. This parameter takes effect only when TriggerType is set to Scheduler.
        # - Pause: Paused.
        # - Skip: Dry run.
        # - Normal: Normal execution.
        self.trigger_recurrence = trigger_recurrence
        # The trigger type.
        # - Scheduler: Triggered by periodic scheduling.
        # - Manual: Triggered manually.
        self.trigger_type = trigger_type
        # The unified workflow instance ID. The value of this field is the same for all task instances within a specific business date under a single trigger.
        self.unified_workflow_instance_id = unified_workflow_instance_id
        # The ID of the workflow to which the task belongs.
        self.workflow_id = workflow_id
        # The ID of the workflow instance.
        self.workflow_instance_id = workflow_instance_id
        # The type of the workflow instance.
        # - SmokeTest: Test.
        # - Manual: Manual task.
        # - SupplementData: Data backfill.
        # - ManualWorkflow: Manual workflow.
        # - Normal: Periodic scheduling.
        # - TriggerWorkflow: Triggered workflow.
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

        if self.ids is not None:
            result['Ids'] = self.ids

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

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

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
            self.ids = m.get('Ids')

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
            self.task_ids = m.get('TaskIds')

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

