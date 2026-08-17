# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListNodeGroupRefreshTasksResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_group_refresh_tasks: List[main_models.ListNodeGroupRefreshTasksResponseBodyNodeGroupRefreshTasks] = None,
        request_id: str = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token for the next query. An empty value indicates that no more results exist.
        self.next_token = next_token
        # The list of node group refresh tasks.
        self.node_group_refresh_tasks = node_group_refresh_tasks
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.node_group_refresh_tasks:
            for v1 in self.node_group_refresh_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NodeGroupRefreshTasks'] = []
        if self.node_group_refresh_tasks is not None:
            for k1 in self.node_group_refresh_tasks:
                result['NodeGroupRefreshTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.node_group_refresh_tasks = []
        if m.get('NodeGroupRefreshTasks') is not None:
            for k1 in m.get('NodeGroupRefreshTasks'):
                temp_model = main_models.ListNodeGroupRefreshTasksResponseBodyNodeGroupRefreshTasks()
                self.node_group_refresh_tasks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNodeGroupRefreshTasksResponseBodyNodeGroupRefreshTasks(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        failed_count: int = None,
        finished_count: int = None,
        max_disruptive_action: str = None,
        node_group_id: str = None,
        node_group_refresh_task_id: str = None,
        start_time: str = None,
        status: str = None,
        total_node_count: int = None,
    ):
        # The end time of the refresh task in ISO 8601 format.
        self.end_time = end_time
        # The number of failed nodes.
        self.failed_count = failed_count
        # The number of finished nodes, including succeeded, failed, and skipped nodes.
        self.finished_count = finished_count
        # The maximum disruptive action level allowed for the refresh operation.
        self.max_disruptive_action = max_disruptive_action
        # The node group ID.
        self.node_group_id = node_group_id
        # The task ID.
        self.node_group_refresh_task_id = node_group_refresh_task_id
        # The start time of the refresh task in ISO 8601 format.
        self.start_time = start_time
        # The task status. Valid values:
        # - Pending: The refresh task is created and waiting to be executed.
        # - InProgress: The refresh task is being processed.
        # - Success: The refresh task is executed.
        # - Failed: The refresh task failed.
        self.status = status
        # The total number of nodes to refresh in this task.
        self.total_node_count = total_node_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count

        if self.max_disruptive_action is not None:
            result['MaxDisruptiveAction'] = self.max_disruptive_action

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_refresh_task_id is not None:
            result['NodeGroupRefreshTaskId'] = self.node_group_refresh_task_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_node_count is not None:
            result['TotalNodeCount'] = self.total_node_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')

        if m.get('MaxDisruptiveAction') is not None:
            self.max_disruptive_action = m.get('MaxDisruptiveAction')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupRefreshTaskId') is not None:
            self.node_group_refresh_task_id = m.get('NodeGroupRefreshTaskId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalNodeCount') is not None:
            self.total_node_count = m.get('TotalNodeCount')

        return self

