# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotaActiveUserUsagesRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        self_only: bool = None,
        sort_by: str = None,
        user_id: str = None,
        username: str = None,
        workload_count: int = None,
        workspace_id: str = None,
    ):
        # The sort order. Valid values:
        # 
        # - `desc`: descending order.
        # 
        # - `asc`: ascending order.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # If true, retrieves resource usage from the current quota only.
        self.self_only = self_only
        # The field to sort the results by. Valid values:
        # 
        # - QuotaId
        # 
        # - SubmittedCPU
        # 
        # - SubmittedMemory
        # 
        # - SubmittedGPU
        # 
        # - UsedCPU
        # 
        # - UsedMemory
        # 
        # - UsedGPU
        # 
        # - WorkloadCount
        self.sort_by = sort_by
        # Filters the results by user ID.
        self.user_id = user_id
        # Filters the results by username.
        self.username = username
        self.workload_count = workload_count
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.self_only is not None:
            result['SelfOnly'] = self.self_only

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        if self.workload_count is not None:
            result['WorkloadCount'] = self.workload_count

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SelfOnly') is not None:
            self.self_only = m.get('SelfOnly')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkloadCount') is not None:
            self.workload_count = m.get('WorkloadCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

