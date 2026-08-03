# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentMemoryRequest(DaraModel):
    def __init__(
        self,
        content_pattern: str = None,
        dmsunit: str = None,
        from_id: str = None,
        mem_from: str = None,
        order: str = None,
        order_by: str = None,
        page_num: int = None,
        page_size: int = None,
        query_all: bool = None,
    ):
        # The content pattern used for fuzzy match search.
        self.content_pattern = content_pattern
        # The current Data Management unit.
        self.dmsunit = dmsunit
        # The source ID.
        # - If MemFrom is set to session, FromId indicates the session ID.
        # - If MemFrom is set to user, FromId indicates the RAM user ID.
        self.from_id = from_id
        # The memory source. Valid values:
        # - session: Generated from a session.
        # - user: Edited by a user.
        self.mem_from = mem_from
        # The sort order for the specified sort field. Default value: desc. Valid values:
        # - asc: Ascending order.
        # - desc: Descending order.
        self.order = order
        # The sort field. Default value: hitTimes. Valid values:
        # - hitTimes: The number of hits.
        # - created: The creation time.
        self.order_by = order_by
        # The page number. Minimum value: 1.
        self.page_num = page_num
        # The maximum number of entries per page. Default value: 50.
        self.page_size = page_size
        # Specifies whether to query memories in all statuses. Default value: true.
        self.query_all = query_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_pattern is not None:
            result['ContentPattern'] = self.content_pattern

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.from_id is not None:
            result['FromId'] = self.from_id

        if self.mem_from is not None:
            result['MemFrom'] = self.mem_from

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_all is not None:
            result['QueryAll'] = self.query_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentPattern') is not None:
            self.content_pattern = m.get('ContentPattern')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')

        if m.get('MemFrom') is not None:
            self.mem_from = m.get('MemFrom')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryAll') is not None:
            self.query_all = m.get('QueryAll')

        return self

