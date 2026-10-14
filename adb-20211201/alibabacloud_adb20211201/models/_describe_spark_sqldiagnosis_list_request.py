# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSparkSQLDiagnosisListRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        max_start_time: str = None,
        min_start_time: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        statement_id: int = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the details of all AnalyticDB for MySQL Data Lakehouse Edition (3.0) clusters in a specific region, including the cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The maximum start time. Format: yyyy-MM-dd HH:mm:ss.
        self.max_start_time = max_start_time
        # The minimum start time. Format: yyyy-MM-dd HH:mm:ss.
        self.min_start_time = min_start_time
        # Sorts the query results by a specified field. The value must be a JSON string. Example: `[{"Field":"MaxExclusiveTime","Type":"Asc"}]`. Parameters in the JSON string:
        # - `Field`: the sort field. Valid values:
        #     - `MaxExclusiveTime`: the maximum execution time.
        #     - `PeakMemory`: the peak memory usage.
        #     - `QueryStartTime`: the query start time.
        #     - `QueryWallclockTime`: the query execution time.
        # 
        # - `Type`: the sort order. Valid values:
        #     - `Asc`: ascending order.
        #     - `Desc`: descending order.
        # 
        # > - If this parameter is not specified, the results are sorted in ascending order by the `MaxExclusiveTime` field by default.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the regions and zones supported by AnalyticDB for MySQL, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The unique ID of the code block in the Spark job.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.max_start_time is not None:
            result['MaxStartTime'] = self.max_start_time

        if self.min_start_time is not None:
            result['MinStartTime'] = self.min_start_time

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('MaxStartTime') is not None:
            self.max_start_time = m.get('MaxStartTime')

        if m.get('MinStartTime') is not None:
            self.min_start_time = m.get('MinStartTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        return self

