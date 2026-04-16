# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryNacosTagsRequest(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        group_by: str = None,
        max_results: int = None,
        need_total_count: bool = None,
        next_token: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.config_type = config_type
        self.group_by = group_by
        self.max_results = max_results
        self.need_total_count = need_total_count
        self.next_token = next_token
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

