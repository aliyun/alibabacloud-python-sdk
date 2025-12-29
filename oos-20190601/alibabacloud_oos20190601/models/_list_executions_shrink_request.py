# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExecutionsShrinkRequest(DaraModel):
    def __init__(
        self,
        categories: str = None,
        category: str = None,
        depth: str = None,
        description: str = None,
        end_date_after: str = None,
        end_date_before: str = None,
        executed_by: str = None,
        execution_id: str = None,
        include_child_execution: bool = None,
        max_results: int = None,
        mode: str = None,
        next_token: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_template_name: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        tags_shrink: str = None,
        template_name: str = None,
    ):
        # The types of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger. You can specify only one of the Categories and Category parameters. We recommend that you specify Categories.
        self.categories = categories
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category
        # The depth of execution. Valid values: RootDepth and FirstChildDepth. If you set this parameter to RootDepth, only the parent execution is returned. If you set this parameter to FirstChildDepth, only the child executions at the first level are returned. You can specify only one of the Depth and IncludeChildExecution parameters. We recommend that you specify Depth.
        self.depth = depth
        # The description of the execution.
        self.description = description
        # The earliest end time. The executions that stop running at or later than the specified time are queried.
        self.end_date_after = end_date_after
        # The latest end time. The executions that stop running at or earlier than the specified time are queried.
        self.end_date_before = end_date_before
        # The executor.
        self.executed_by = executed_by
        # The ID of the execution.
        self.execution_id = execution_id
        # Specifies whether to include child executions. Default value: False.
        self.include_child_execution = include_child_execution
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The execution mode. Valid values:
        # 
        # *   **Automatic**
        # *   **Debug**
        self.mode = mode
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group to which the instances you want to query belong.
        self.resource_group_id = resource_group_id
        # The ID of the Elastic Compute Service (ECS) resource.
        self.resource_id = resource_id
        # The name of the resource template.
        self.resource_template_name = resource_template_name
        # The field that is used to sort the executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the executions are sorted based on the time when they stop running.
        # *   **Status**: specifies that the executions are sorted based on their states.
        self.sort_field = sort_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order
        # The earliest start time. The executions that start to run at or later than the specified time are queried.
        self.start_date_after = start_date_after
        # The latest start time. The executions that start to run at or earlier than the specified point in time are queried.
        self.start_date_before = start_date_before
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.status = status
        # The tags for the execution.
        self.tags_shrink = tags_shrink
        # The name of the template. All templates whose names contain the specified template name are queried.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.category is not None:
            result['Category'] = self.category

        if self.depth is not None:
            result['Depth'] = self.depth

        if self.description is not None:
            result['Description'] = self.description

        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after

        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before

        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after

        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before

        if self.status is not None:
            result['Status'] = self.status

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')

        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')

        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')

        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

