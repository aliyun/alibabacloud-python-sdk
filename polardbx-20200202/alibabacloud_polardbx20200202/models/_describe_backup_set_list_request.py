# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupSetListRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region where the backup sets reside. If you specify this parameter, backup sets in the specified region are returned. You can specify only one region at a time.
        self.dest_cross_region = dest_cross_region
        # The end time. Specify a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The page number. The value starts from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time. Specify a UNIX timestamp in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

