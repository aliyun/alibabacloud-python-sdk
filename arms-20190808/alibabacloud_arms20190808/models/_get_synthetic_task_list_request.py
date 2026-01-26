# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSyntheticTaskListRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        task_name: str = None,
        task_status: str = None,
        task_type: str = None,
        url: str = None,
    ):
        # The order by which the queried tasks are sorted. Valid values:
        # 
        # *   **asc**: ascending
        # *   **desc**: descending
        self.direction = direction
        # The condition by which the queried tasks are sorted.
        self.order = order
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The region ID. Default value: **cn-hangzhou**.
        self.region_id = region_id
        # The task name.
        self.task_name = task_name
        # The status of the task. Valid values:
        # 
        # *   **0**: The task is stopped.
        # *   **1**: The task is started.
        # *   **9**: The task is ended.
        self.task_status = task_status
        # The type of the task. Valid values:
        # 
        # 1.  3: web page performance - IE
        # 2.  34: web page performance - Chrome
        # 3.  0: network quality
        # 4.  40: file download
        # 5.  7: API performance
        self.task_type = task_type
        # The URL for synthetic monitoring.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.order is not None:
            result['Order'] = self.order

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

