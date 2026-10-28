# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSqlPatternRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sql_pattern: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The cluster ID.
        # > You can call the DescribeDBClusters operation to query the IDs of all clusters in a specified region.
        # [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html)
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies the sorting of query results by a specified field. The format is a JSON character string, such as `[{"Field":"Pattern","Type":"Asc"}]`. Parameters:
        # - Field: the sorting field. Valid values:
        #     - Pattern: SQL pattern.
        #     - AccessIP: client IP address.
        #     - User: username.
        #     - QueryCount: total number of queries.
        #     - AvgPeakMemory: average peak memory. Unit: KB.
        #     - MaxPeakMemory: Peak Volume memory. Unit: KB.
        #     - AvgCpuTime: average computing duration. Unit: milliseconds.
        #     - MaxCpuTime: maximum computing duration. Unit: milliseconds.
        #     - AvgStageCount: average number of stages.
        #     - MaxStageCount: maximum number of stages.
        #     - AvgTaskCount: average number of tasks.
        #     - MaxTaskCount: maximum number of tasks.
        #     - AvgScanSize: average scan size. Unit: KB.
        #     - MaxScanSize: maximum scan size. Unit: KB.
        # 
        # - Type: the sorting method. Valid values:
        #     - Asc: ascending sorting.
        #     - Desc: descending sorting.
        # 
        # > - If no Settings are specified for this parameter, the results are sorted in ascending order by the Pattern field by default.
        # - To perform sorting by the AccessIP field, you must set the Type parameter to accessip. To perform sorting by the User field, you must leave the Type parameter empty or set it to user.
        self.order = order
        # The page number. Valid values: integers greater than 0 and no greater than the maximum value of the Integer type.
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - **10** (default)
        # - **30**
        # - **50**
        # - **100**
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The keyword that the SQL pattern must contain.
        # > If this parameter is not specified, the details of all SQL patterns for the cluster on the date specified by the StartTime parameter are returned by default.
        self.sql_pattern = sql_pattern
        # The start date of the query. The time is in UTC and formatted as yyyy-MM-dd.
        # > You can only query data within the last 30 days.
        self.start_time = start_time
        # Aggregates SQL patterns by a specified dimension. Valid values:
        #  - user: aggregates by user.
        #  - accessip: aggregates by access IP address.
        # 
        # > If this parameter is not specified, SQL patterns are aggregated by user by default.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sql_pattern is not None:
            result['SqlPattern'] = self.sql_pattern

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SqlPattern') is not None:
            self.sql_pattern = m.get('SqlPattern')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

