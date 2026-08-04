# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserViewMetricsRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
        time_step: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The sort order. Valid values:
        # - asc: ascending order.
        # - desc: descending order.
        self.order = order
        # The current page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The page size.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The sorting criterion.
        self.sort_by = sort_by
        # The time step. Default value: 5m. Valid values for the time unit:
        # 
        # - h: hours.
        # 
        # - m: minutes.
        # 
        # - s: seconds.
        # 
        # If no unit is specified, the default unit s (seconds) is used.
        self.time_step = time_step
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id
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

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.time_step is not None:
            result['TimeStep'] = self.time_step

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

