# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMetaProfilingSkillJobPageRequest(DaraModel):
    def __init__(
        self,
        component_ids: List[int] = None,
        ds_id: int = None,
        ds_name: str = None,
        ds_type: str = None,
        group_by: str = None,
        is_display_system_task: bool = None,
        job_id: int = None,
        job_name: str = None,
        need_total_count: bool = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # The list of component IDs used to filter profiling tasks by multiple data source components.
        self.component_ids = component_ids
        # The data source ID.
        self.ds_id = ds_id
        # The data source name.
        self.ds_name = ds_name
        # The data source type identifier.
        self.ds_type = ds_type
        # The name of the grouping field used for aggregation.
        self.group_by = group_by
        # Specifies whether to display system built-in tasks.
        self.is_display_system_task = is_display_system_task
        # The profiling task ID.
        self.job_id = job_id
        # The profiling task name.
        self.job_name = job_name
        # Specifies whether to return the total number of records.
        self.need_total_count = need_total_count
        # The name of the sort field.
        self.order_by = order_by
        # The sort direction, such as ascending (ASC) or descending (DESC).
        self.order_direction = order_direction
        # The current page number, starting from 1.
        self.page_index = page_index
        # The number of records to return per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_ids is not None:
            result['componentIds'] = self.component_ids

        if self.ds_id is not None:
            result['dsId'] = self.ds_id

        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.is_display_system_task is not None:
            result['isDisplaySystemTask'] = self.is_display_system_task

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_name is not None:
            result['jobName'] = self.job_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentIds') is not None:
            self.component_ids = m.get('componentIds')

        if m.get('dsId') is not None:
            self.ds_id = m.get('dsId')

        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('isDisplaySystemTask') is not None:
            self.is_display_system_task = m.get('isDisplaySystemTask')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

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

        return self

