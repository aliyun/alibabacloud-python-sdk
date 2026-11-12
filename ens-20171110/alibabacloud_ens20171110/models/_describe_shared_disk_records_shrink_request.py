# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSharedDiskRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        disk_ids_shrink: str = None,
        end_time: str = None,
        namespaces_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids_shrink: str = None,
        sdg_ids_shrink: str = None,
        start_time: str = None,
    ):
        # The shared disk IDs.
        self.disk_ids_shrink = disk_ids_shrink
        # The billing end time.
        self.end_time = end_time
        # The namespaces.
        self.namespaces_shrink = namespaces_shrink
        # The page number for the paging query.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region IDs.
        self.region_ids_shrink = region_ids_shrink
        # The SDG IDs.
        self.sdg_ids_shrink = sdg_ids_shrink
        # The billing start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_ids_shrink is not None:
            result['DiskIds'] = self.disk_ids_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.namespaces_shrink is not None:
            result['Namespaces'] = self.namespaces_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink

        if self.sdg_ids_shrink is not None:
            result['SdgIds'] = self.sdg_ids_shrink

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids_shrink = m.get('DiskIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Namespaces') is not None:
            self.namespaces_shrink = m.get('Namespaces')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')

        if m.get('SdgIds') is not None:
            self.sdg_ids_shrink = m.get('SdgIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

