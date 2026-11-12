# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatabaseInstancesRequest(DaraModel):
    def __init__(
        self,
        database_instance_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IDs of the lightweight database instances. The value can be a JSON array that consists of multiple instance IDs. You can specify up to 100 instance IDs. Separate multiple IDs with commas (,).
        self.database_instance_ids = database_instance_ids
        # The page number of the lightweight database instance list.
        # 
        # Starting value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the lightweight database instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_instance_ids is not None:
            result['DatabaseInstanceIds'] = self.database_instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceIds') is not None:
            self.database_instance_ids = m.get('DatabaseInstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

