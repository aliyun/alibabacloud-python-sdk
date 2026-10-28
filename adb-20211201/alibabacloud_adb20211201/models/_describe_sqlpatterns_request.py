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
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the details of all AnalyticDB for MySQL Data Lakehouse Edition clusters in a specified region, including the cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in UTC in the <i>yyyy-MM-ddTHH:mm:ssZ</i> format.
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The search keyword.
        self.keyword = keyword
        # The language configuration. Valid values:
        # - **zh**: Simplified Chinese (default language).
        # - **en**: English.
        # - **ja**: Japanese.
        # - **zh-tw**: Traditional Chinese.
        self.lang = lang
        # The sorting rule for the query results. The format is a JSON character string. Example: `[{"Field":"AverageQueryTime","Type":"Asc"}]`. The JSON character string contains the following parameters:
        # - `Field`: the field by which to sort the results. Valid values:
        #     - `PatternCreationTime`: the earliest commit time of the pattern within the query time range.
        #     - `AverageQueryTime`: the average total time consumed by the pattern within the query time range.
        #     - `MaxQueryTime`: the maximum total time consumed by the pattern within the query time range.
        #     - `AverageExecutionTime`: the average execution duration of the pattern within the query time range.
        #     - `MaxExecutionTime`: the maximum execution duration of the pattern within the query time range.
        #     - `AveragePeakMemory`: the average peak memory usage of the pattern within the query time range.
        #     - `MaxPeakMemory`: the maximum peak memory usage of the pattern within the query time range.
        #     - `AverageScanSize`: the average amount of data read by the pattern within the query time range.
        #     - `MaxScanSize`: the maximum amount of data read by the pattern within the query time range.
        #     - `QueryCount`: the number of executions of the pattern within the query time range.
        #     - `FailedCount`: the number of failed executions of the pattern within the query time range.
        # 
        # - `Type`: the sort order. The value is not case-sensitive. Valid values:
        #     - `Asc`: ascending order.
        #     - `Desc`: descending order.
        self.order = order
        # The page number. Valid values: integers greater than 0 and up to the maximum integer value.
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - **10** (default value)
        # - **30**
        # - **50**
        # - **100**
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The hash value of the SQL pattern, which is used to filter a specific SQL pattern.
        self.sql_pattern_hash = sql_pattern_hash
        # The start time of the query. Specify the time in UTC in the <i>yyyy-MM-ddTHH:mm:ssZ</i> format.
        # >  - You can only query data from the last 14 days.
        # - The interval between the start time and the end time cannot exceed 24 hours.
        self.start_time = start_time
        # The name of the database account that executes the SQL statement.
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

