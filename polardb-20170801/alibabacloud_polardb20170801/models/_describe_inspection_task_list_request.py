# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInspectionTaskListRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        space_id: str = None,
    ):
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30.
        self.page_size = page_size
        # The ID of the region where the task is located.
        self.region_id = region_id
        # The ID of the inspection space used to filter tasks.
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        return self

