# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTaskExecutionsRequest(DaraModel):
    def __init__(
        self,
        end_date_after: str = None,
        end_date_before: str = None,
        execution_id: str = None,
        include_child_task_execution: bool = None,
        max_results: int = None,
        next_token: str = None,
        parent_task_execution_id: str = None,
        region_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # The execution ID of the task.
        self.end_date_after = end_date_after
        # Specifies to query task executions that stop running at or later than the specified time.
        self.end_date_before = end_date_before
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.execution_id = execution_id
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.include_child_task_execution = include_child_task_execution
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results
        # Sorts the task executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the task executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the task executions are sorted based on the time when the time when they stop running.
        # *   **Status**: specifies that the task executions are sorted based on their statuses.
        self.next_token = next_token
        # Specifies whether to show the child nodes in the loop task. Default value: False.
        self.parent_task_execution_id = parent_task_execution_id
        # The ID of the execution.
        self.region_id = region_id
        # The order in which you want to sort the task executions to query. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_field = sort_field
        # The token that is used to retrieve the next page of results.
        self.sort_order = sort_order
        # Specifies to query task executions that stop running at or before the specified time.
        self.start_date_after = start_date_after
        # Specifies to query task executions that start to run at or later than the specified time.
        self.start_date_before = start_date_before
        # Specifies to query task executions that start to run at or before the specified time.
        self.status = status
        # The execution ID of the parent node. In a loop task, set this parameter to the execution ID of the parent node.
        self.task_action = task_action
        # The name of the task.
        self.task_execution_id = task_execution_id
        # The action of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after

        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.include_child_task_execution is not None:
            result['IncludeChildTaskExecution'] = self.include_child_task_execution

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')

        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('IncludeChildTaskExecution') is not None:
            self.include_child_task_execution = m.get('IncludeChildTaskExecution')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

