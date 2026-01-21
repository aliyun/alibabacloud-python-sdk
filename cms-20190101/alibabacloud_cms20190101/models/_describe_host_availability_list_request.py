# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHostAvailabilityListRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        id: int = None,
        ids: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        task_name: str = None,
    ):
        # The ID of the application group.
        self.group_id = group_id
        # The ID of the availability monitoring task.
        self.id = id
        # The IDs of the availability monitoring tasks. Separate multiple IDs with commas (,).
        self.ids = ids
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Minimum value: 1. Default value: 10
        self.page_size = page_size
        self.region_id = region_id
        # The name of the availability monitoring task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

