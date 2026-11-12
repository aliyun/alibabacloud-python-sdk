# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSharedDiskRecordsRequest(DaraModel):
    def __init__(
        self,
        disk_ids: List[str] = None,
        end_time: str = None,
        namespaces: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: List[str] = None,
        sdg_ids: List[str] = None,
        start_time: str = None,
    ):
        # The shared disk IDs.
        self.disk_ids = disk_ids
        # The billing end time.
        self.end_time = end_time
        # The namespaces.
        self.namespaces = namespaces
        # The page number for the paging query.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region IDs.
        self.region_ids = region_ids
        # The SDG IDs.
        self.sdg_ids = sdg_ids
        # The billing start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.sdg_ids is not None:
            result['SdgIds'] = self.sdg_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('SdgIds') is not None:
            self.sdg_ids = m.get('SdgIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

