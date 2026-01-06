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
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The order by which to sort query results. Specify the parameter value in the JSON string format. Example: `[{"Field":"Pattern","Type":"Asc"}]`. Parameters:
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `Pattern`: the SQL pattern.
        #     *   `AccessIP`: the IP address of the client.
        #     *   `User`: the username.
        #     *   `QueryCount`: the number of queries performed in association with the SQL pattern within the time range to query.
        #     *   `AvgPeakMemory`: the average peak memory usage of the SQL pattern within the time range to query. Unit: KB.
        #     *   `MaxPeakMemory`: the maximum peak memory usage of the SQL pattern within the time range to query. Unit: KB.
        #     *   `AvgCpuTime`: the average execution duration of the SQL pattern within the time range to query. Unit: milliseconds.
        #     *   `MaxCpuTime`: the maximum execution duration of the SQL pattern within the time range to query. Unit: milliseconds.
        #     *   `AvgStageCount`: the average number of stages.
        #     *   `MaxStageCount`: the maximum number of stages.
        #     *   `AvgTaskCount`: the average number of tasks.
        #     *   `MaxTaskCount`: the maximum number of tasks.
        #     *   `AvgScanSize`: the average amount of data scanned based on the SQL pattern within the time range to query. Unit: KB.
        #     *   `MaxScanSize`: the maximum amount of data scanned based on the SQL pattern within the time range to query. Unit: KB.
        # 
        # *   `Type` specifies the sorting order. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, query results are sorted in ascending order of `Pattern`.
        # 
        # *   If you want to sort query results by `AccessIP`, you must set the `Type` parameter to `accessip`. If you want to sort query results by `User`, you must leave the `Type` parameter empty or set it to `user`.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **10** (default)
        # *   **30**
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The keyword that is used for the query.
        # 
        # > If you do not specify this parameter, all SQL patterns of the AnalyticDB for MySQL cluster within the time period specified by `StartTime` are returned.
        self.sql_pattern = sql_pattern
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd format. The time must be in UTC.
        # 
        # > Only data within the last 30 days can be queried.
        self.start_time = start_time
        # The dimension by which to aggregate the SQL patterns. Valid values:
        # 
        # *   `user`: aggregates the SQL patterns by user.
        # *   `accessip`: aggregates the SQL patterns by client IP address.
        # 
        # > If you do not specify this parameter, the SQL patterns are aggregated by `user`.
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

