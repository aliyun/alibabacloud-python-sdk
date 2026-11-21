# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMaintainWindowsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        enable: bool = None,
        maintain_window_id: str = None,
        maintain_window_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        workspace: str = None,
    ):
        # The sort order. Valid values:
        # 
        # - **asc**: Ascending order.
        # - **desc**: Descending order. This is the default value.
        self.direction = direction
        # Filters by enabled status. Valid values:
        # 
        # - **true**: Returns only enabled silence policies.
        # - **false**: Returns only paused silence policies.
        # 
        # If you do not specify this parameter, the policies are not filtered by enabled status.
        self.enable = enable
        # The ID of the silence policy. Exact matching is used. If you do not specify this parameter, the policies are not filtered by ID.
        self.maintain_window_id = maintain_window_id
        # Policy Name of the silence policy. Fuzzy matching is used, where a match occurs if Policy Name contains the specified value. If you do not specify this parameter, the policies are not filtered by name.
        self.maintain_window_name = maintain_window_name
        # The maximum number of records to return for this request. Default value: 20.
        self.max_results = max_results
        # The pagination cursor. You do not need to specify this parameter for the first query. For subsequent queries, you can specify the non-empty nextToken returned in the previous response. This value does not guarantee that the next page contains data.
        self.next_token = next_token
        # The field by which to sort. By default, the policies are sorted by creation time. Valid values:
        # 
        # - **createTime**: Creation time.
        # - **updateTime**: Update time.
        # - **enable**: Enabled status.
        # 
        # If you specify other values, the policies are sorted by creation time.
        self.order_by = order_by
        # The name of the workspace. This parameter is required by the backend and is used to isolate silence policy resources across different business workspaces.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['direction'] = self.direction

        if self.enable is not None:
            result['enable'] = self.enable

        if self.maintain_window_id is not None:
            result['maintainWindowId'] = self.maintain_window_id

        if self.maintain_window_name is not None:
            result['maintainWindowName'] = self.maintain_window_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('maintainWindowId') is not None:
            self.maintain_window_id = m.get('maintainWindowId')

        if m.get('maintainWindowName') is not None:
            self.maintain_window_name = m.get('maintainWindowName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

