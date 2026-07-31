# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLPatternsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sql_pattern_hash: int = None,
        start_time: str = None,
        user_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL (Data Lakehouse Edition) cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) API to find the cluster IDs of all AnalyticDB for MySQL (Data Lakehouse Edition) clusters in a specific region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. The time must be in UTC and formatted as *yyyy-MM-ddTHH:mm:ssZ*.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The keyword for filtering the query results.
        self.keyword = keyword
        # The response language. Valid values:
        # 
        # - **zh**: Simplified Chinese (default)
        # 
        # - **en**: English
        # 
        # - **ja**: Japanese
        # 
        # - **zh-tw**: Traditional Chinese
        self.lang = lang
        # The sort order for the results. Specify this parameter as a JSON string, for example, `[{"Field":"AverageQueryTime","Type":"Asc"}]`. The string consists of the following fields:
        # 
        # - `Field`: the sort field. Valid values:
        # 
        #   - `PatternCreationTime`: The earliest submission time of the pattern.
        # 
        #   - `AverageQueryTime`: The average query time of the pattern.
        # 
        #   - `MaxQueryTime`: The maximum query time of the pattern.
        # 
        #   - `AverageExecutionTime`: The average execution time of the pattern.
        # 
        #   - `MaxExecutionTime`: The maximum execution time of the pattern.
        # 
        #   - `AveragePeakMemory`: The average peak memory of the pattern.
        # 
        #   - `MaxPeakMemory`: The maximum peak memory of the pattern.
        # 
        #   - `AverageScanSize`: The average scanned data size of the pattern.
        # 
        #   - `MaxScanSize`: The maximum scanned data size of the pattern.
        # 
        #   - `QueryCount`: The query count of the pattern.
        # 
        #   - `FailedCount`: The failure count of the pattern.
        # 
        # - `Type`: the sort order. Valid values (case-insensitive):
        # 
        #   - `Asc`: ascending order.
        # 
        #   - `Desc`: descending order.
        self.order = order
        # The page number. Must be an integer greater than 0. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **10** (default)
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.sql_pattern_hash = sql_pattern_hash
        # The start of the time range to query. The time must be in UTC and formatted as *yyyy-MM-ddTHH:mm:ssZ*.
        # 
        # > - Data is available for the last 14 days only.
        # 
        # - The time range cannot exceed 24 hours.
        self.start_time = start_time
        # The username of the database account used to execute the SQL statements.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sql_pattern_hash is not None:
            result['SqlPatternHash'] = self.sql_pattern_hash

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SqlPatternHash') is not None:
            self.sql_pattern_hash = m.get('SqlPatternHash')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

