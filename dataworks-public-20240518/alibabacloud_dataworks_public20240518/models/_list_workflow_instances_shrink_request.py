# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkflowInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_date: int = None,
        env_type: str = None,
        filter: str = None,
        ids_shrink: str = None,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        tags_shrink: str = None,
        type: str = None,
        unified_workflow_instance_id: int = None,
        workflow_id: int = None,
    ):
        # The business date. This is generally 00:00:00 of the day before the scheduled instance trigger time, in millisecond-level timestamp format, such as 1743350400000.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        self.env_type = env_type
        # The filter. In JSON format, multiple filter conditions have an AND relationship. Currently supported fields are: `status, executionDate`.
        self.filter = filter
        # The list of workflow instance IDs. You can use this parameter to query multiple workflow instances at a time.
        self.ids_shrink = ids_shrink
        # The name. Fuzzy match is supported.
        self.name = name
        # The account ID of the owner.
        self.owner = owner
        # The page number, starting from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of sort fields. Sorting by trigger time, start time, and other fields is supported. The format is "sort field + sort order (Desc/Asc)" (Asc can be omitted). Valid values of the sort field:
        # 
        # - TriggerTime (Desc/Asc)
        # 
        # - StartedTime (Desc/Asc)
        # 
        # - FinishedTime (Desc/Asc)
        # 
        # - CreateTime (Desc/Asc)
        # 
        # - Id (Desc/Asc)
        # 
        # Default value: Id Desc
        self.sort_by = sort_by
        # The list of tags. Results are returned if any one of the specified tags is matched.
        self.tags_shrink = tags_shrink
        # The type of the workflow instance.
        # 
        # - Normal: Periodic scheduling
        # 
        # - Manual: Manual task
        # 
        # - SmokeTest: Testing
        # 
        # - SupplementData: Backfill data
        # 
        # - ManualWorkflow: Manual workflow
        # 
        # - TriggerWorkflow: Trigger-based workflow
        self.type = type
        # The unified workflow instance ID. All workflow instances within the same business date of a single trigger share the same value for this field.
        self.unified_workflow_instance_id = unified_workflow_instance_id
        # The ID of the workflow to which the instance belongs.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.type is not None:
            result['Type'] = self.type

        if self.unified_workflow_instance_id is not None:
            result['UnifiedWorkflowInstanceId'] = self.unified_workflow_instance_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UnifiedWorkflowInstanceId') is not None:
            self.unified_workflow_instance_id = m.get('UnifiedWorkflowInstanceId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

