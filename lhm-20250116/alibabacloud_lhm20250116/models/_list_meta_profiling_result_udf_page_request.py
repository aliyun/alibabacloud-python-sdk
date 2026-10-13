# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaProfilingResultUdfPageRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        component_type: int = None,
        db_name: str = None,
        func_name: str = None,
        group_by: str = None,
        is_summary: bool = None,
        need_total_count: bool = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.catalog_name = catalog_name
        self.component_type = component_type
        self.db_name = db_name
        self.func_name = func_name
        self.group_by = group_by
        self.is_summary = is_summary
        self.need_total_count = need_total_count
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.func_name is not None:
            result['funcName'] = self.func_name

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.is_summary is not None:
            result['isSummary'] = self.is_summary

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('funcName') is not None:
            self.func_name = m.get('funcName')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('isSummary') is not None:
            self.is_summary = m.get('isSummary')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

