# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceMissingIndexListRequest(DaraModel):
    def __init__(
        self,
        avg_total_user_cost: str = None,
        avg_user_impact: str = None,
        end_time: str = None,
        index_count: str = None,
        instance_id: str = None,
        object_name: str = None,
        page_no: str = None,
        page_size: str = None,
        reserved_pages: str = None,
        reserved_size: str = None,
        row_count: str = None,
        start_time: str = None,
        unique_compiles: str = None,
        user_scans: str = None,
        user_seeks: str = None,
    ):
        # The query condition based on the average cost savings.
        self.avg_total_user_cost = avg_total_user_cost
        # The query condition based on the performance improvement.
        self.avg_user_impact = avg_user_impact
        # The end time of the last seek.
        self.end_time = end_time
        # The query condition based on the number of indexes.
        self.index_count = index_count
        # The database instance ID.
        # 
        # >  Only ApsaraDB RDS for SQL Server instances are supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The object name.
        self.object_name = object_name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The query condition based on the total number of pages.
        self.reserved_pages = reserved_pages
        # The query condition based on the table size.
        self.reserved_size = reserved_size
        # The query condition based on the number of table rows.
        self.row_count = row_count
        # The start time of the last seek.
        self.start_time = start_time
        # The query condition based on the number of compilations.
        self.unique_compiles = unique_compiles
        # The query condition based on the number of scans.
        self.user_scans = user_scans
        # The query condition based on the number of seeks.
        self.user_seeks = user_seeks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_total_user_cost is not None:
            result['AvgTotalUserCost'] = self.avg_total_user_cost

        if self.avg_user_impact is not None:
            result['AvgUserImpact'] = self.avg_user_impact

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.index_count is not None:
            result['IndexCount'] = self.index_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reserved_pages is not None:
            result['ReservedPages'] = self.reserved_pages

        if self.reserved_size is not None:
            result['ReservedSize'] = self.reserved_size

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.unique_compiles is not None:
            result['UniqueCompiles'] = self.unique_compiles

        if self.user_scans is not None:
            result['UserScans'] = self.user_scans

        if self.user_seeks is not None:
            result['UserSeeks'] = self.user_seeks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgTotalUserCost') is not None:
            self.avg_total_user_cost = m.get('AvgTotalUserCost')

        if m.get('AvgUserImpact') is not None:
            self.avg_user_impact = m.get('AvgUserImpact')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IndexCount') is not None:
            self.index_count = m.get('IndexCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReservedPages') is not None:
            self.reserved_pages = m.get('ReservedPages')

        if m.get('ReservedSize') is not None:
            self.reserved_size = m.get('ReservedSize')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UniqueCompiles') is not None:
            self.unique_compiles = m.get('UniqueCompiles')

        if m.get('UserScans') is not None:
            self.user_scans = m.get('UserScans')

        if m.get('UserSeeks') is not None:
            self.user_seeks = m.get('UserSeeks')

        return self

