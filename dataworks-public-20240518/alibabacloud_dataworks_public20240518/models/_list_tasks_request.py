# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTasksRequest(DaraModel):
    def __init__(
        self,
        ids: List[int] = None,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_env: str = None,
        project_id: int = None,
        runtime_resource: str = None,
        sort_by: str = None,
        task_type: str = None,
        trigger_recurrence: str = None,
        trigger_type: str = None,
        workflow_id: int = None,
    ):
        # The ID of the task.
        self.ids = ids
        # The name of the task. Fuzzy match is supported.
        self.name = name
        # The account ID of the task owner.
        self.owner = owner
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The workspace environment.
        # 
        # Valid values:
        # 
        # *   Prod
        # *   Dev
        self.project_env = project_env
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The information about the resource group. Set this parameter to the ID of a resource group for scheduling.
        self.runtime_resource = runtime_resource
        # The field that is used to sort tasks. This parameter is configured in the format of "Sorting field Sorting order". You can set the sorting order to Desc or Asc. If you do not specify the sorting order, Asc is used by default. Valid values:
        # 
        # *   `ModifyTime (Desc/Asc)`
        # 
        # *   `CreateTime (Desc/Asc)`
        # 
        # *   `Id (Desc/Asc)`
        # 
        #     Default value: `Id Desc`.
        self.sort_by = sort_by
        # The type of the task. Valid values:
        # 
        # *   ODPS_SQL
        # *   SPARK
        # *   PY_ODPS
        # *   PY_ODPS3
        # *   ODPS_SCRIPT
        # *   ODPS_MR
        # *   COMPONENT_SQL
        # *   EMR_HIVE
        # *   EMR_MR
        # *   EMR_SPARK_SQL
        # *   EMR_SPARK
        # *   EMR_SHELL
        # *   EMR_PRESTO
        # *   EMR_IMPALA
        # *   SPARK_STREAMING
        # *   EMR_KYUUBI
        # *   EMR_TRINO
        # *   HOLOGRES_SQL
        # *   HOLOGRES_SYNC_DDL
        # *   HOLOGRES_SYNC_DATA
        self.task_type = task_type
        # The run mode when triggered. Valid only if TriggerType is Scheduler.
        # 
        # Valid values:
        # 
        # *   Pause
        # *   Skip
        # *   Normal
        self.trigger_recurrence = trigger_recurrence
        # The trigger type.
        # 
        # Valid values:
        # 
        # *   Scheduler: Triggered by schedule.
        # *   Manual: Triggered manually.
        self.trigger_type = trigger_type
        # The ID of the workflow to which the task belongs.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.name is not None:
            result['Name'] = self.name

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

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.trigger_recurrence is not None:
            result['TriggerRecurrence'] = self.trigger_recurrence

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TriggerRecurrence') is not None:
            self.trigger_recurrence = m.get('TriggerRecurrence')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

