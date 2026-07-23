# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRoutineBuildsRequest(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        routine_name: str = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
    ):
        # The page number for a paged query. The value must be greater than or equal to 1.
        self.page_index = page_index
        # The number of entries per page for a paged query. Valid values: 1 to 500.
        self.page_size = page_size
        # The ER name.
        self.routine_name = routine_name
        # The field used for sorting. By default, results are sorted by purchase time. Valid values:
        # 
        # - CreateTime: purchase time.
        # - ExpireTime: expiration time.
        self.sort_by = sort_by
        # The sort order. Default value: desc. Valid values:
        # 
        # - asc: ascending order.
        # - desc: descending order.
        self.sort_order = sort_order
        # The status of the build task. Valid values:
        # 
        # - int: initialization
        # - pending: preparing
        # - building: building
        # - succeed: build succeeded
        # - failed: build failed
        # - canceled: canceled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

