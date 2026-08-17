# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNodeGroupRefreshTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_group_refresh_task_id: str = None,
        node_statuses_shrink: str = None,
    ):
        # The maximum number of entries per page for a paged query. Valid values: 1 to 500. Default value: 100. For more information about paging, set this parameter together with NextToken.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request. This parameter is used to paginate through the node list in the current refresh task.
        self.next_token = next_token
        # The ID of the refresh task.
        # 
        # This parameter is required.
        self.node_group_refresh_task_id = node_group_refresh_task_id
        # The node refresh statuses to filter by. Valid values:
        # - Pending: the node is waiting to be refreshed.
        # - InProgress: the node is being refreshed.
        # - Success: the node is refreshed.
        # - Failed: the node failed to be refreshed.
        # - Skipped: all properties to be refreshed on the node exceeded the MaxDisruptiveAction constraint and were skipped.
        self.node_statuses_shrink = node_statuses_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_refresh_task_id is not None:
            result['NodeGroupRefreshTaskId'] = self.node_group_refresh_task_id

        if self.node_statuses_shrink is not None:
            result['NodeStatuses'] = self.node_statuses_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupRefreshTaskId') is not None:
            self.node_group_refresh_task_id = m.get('NodeGroupRefreshTaskId')

        if m.get('NodeStatuses') is not None:
            self.node_statuses_shrink = m.get('NodeStatuses')

        return self

