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
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL Data Lakehouse Edition clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The latest start time.
        self.max_start_time = max_start_time
        # The earliest start time.
        self.min_start_time = min_start_time
        # The order by which to sort query results. Specify the parameter value in the JSON format. Example: `[{"Field":"MaxExclusiveTime","Type":"Asc"}]`.
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `MaxExclusiveTime`: the maximum execution duration.
        #     *   `PeakMemory`: the peak memory.
        #     *   `QueryStartTime`: the start time of the query.
        #     *   `QueryWallclockTime`: the execution duration of the query.
        # 
        # *   `Type` specifies the sorting order. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, query results are sorted by `MaxExclusiveTime` in ascending order.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
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

