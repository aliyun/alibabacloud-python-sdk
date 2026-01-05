# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWorkflowInstancesRequest(DaraModel):
    def __init__(
        self,
        biz_date: int = None,
        filter: str = None,
        ids: List[int] = None,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        tags: List[str] = None,
        type: str = None,
        unified_workflow_instance_id: int = None,
        workflow_id: int = None,
    ):
        # The data timestamp. The value of this parameter is 00:00:00 of the day before the scheduling time of the instance. The value is a UNIX timestamp. Unit: milliseconds. Example: 1743350400000.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        self.filter = filter
        # The IDs of the workflow instances. You can query multiple instances at a time by instance ID.
        self.ids = ids
        # The instance name. Fuzzy match is supported.
        self.name = name
        # The account ID of the workflow instance owner.
        self.owner = owner
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The fields used for sorting. Fields such as TriggerTime and StartedTime are supported. The value of this parameter is in the Sort field + Sort by (Desc/Asc) format. By default, results are sorted in ascending order. Valid values:
        # 
        # *   TriggerTime (Desc/Asc)
        # *   StartedTime (Desc/Asc)
        # *   FinishedTime (Desc/Asc)
        # *   CreateTime (Desc/Asc)
        # *   Id (Desc/Asc)
        # 
        # Default value: Id Desc.
        self.sort_by = sort_by
        self.tags = tags
        # The type of the workflow instance. Valid values:
        # 
        # *   Normal: Scheduled execution
        # *   Manual: Manually triggered node
        # *   SmokeTest: Smoke test
        # *   SupplementData: Data backfill
        # *   ManualWorkflow: Manually triggered workflow
        # *   TriggerWorkflow: Triggered Workflow
        self.type = type
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

        if self.filter is not None:
            result['Filter'] = self.filter

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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.tags is not None:
            result['Tags'] = self.tags

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

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UnifiedWorkflowInstanceId') is not None:
            self.unified_workflow_instance_id = m.get('UnifiedWorkflowInstanceId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

