# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNodeGroupRefreshTasksRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
        statuses: List[str] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The maximum number of entries per page for paging. Valid values: 1 to 500. Default value: 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The node group ID.
        self.node_group_id = node_group_id
        # The list of task statuses. Valid values:
        # - Pending: The refresh task is created and waiting to be executed.
        # - InProgress: The refresh task is being processed.
        # - Success: The refresh task is executed.
        # - Failed: The refresh task failed.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

