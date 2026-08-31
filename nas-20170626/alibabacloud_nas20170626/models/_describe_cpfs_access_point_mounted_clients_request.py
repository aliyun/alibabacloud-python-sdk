# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCpfsAccessPointMountedClientsRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        file_system_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The access point ID.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The page number of the list.
        self.page_number = page_number
        # The number of results on each page. Valid values: 1 to 100.
        # Default value: 10.
        self.page_size = page_size
        # The region ID.
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
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

