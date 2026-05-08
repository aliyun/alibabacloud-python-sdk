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
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL clusters in a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The keyword that is used for the query.
        self.keyword = keyword
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The order by which to sort query results. Specify the parameter value in the JSON format. Example: `[{"Field":"AverageQueryTime","Type":"Asc"}]`.
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `PatternCreationTime`: the earliest commit time of the SQL pattern within the time range to query.
        #     *   `AverageQueryTime`: the average total amount of time consumed by the SQL pattern within the time range to query.
        #     *   `MaxQueryTime`: the maximum total amount of time consumed by the SQL pattern within the time range to query.
        #     *   `AverageExecutionTime`: the average execution duration of the SQL pattern within the time range to query.
        #     *   `MaxExecutionTime`: the maximum execution duration of the SQL pattern within the time range to query.
        #     *   `AveragePeakMemory`: the average peak memory usage of the SQL pattern within the time range to query.
        #     *   `MaxPeakMemory`: the maximum peak memory usage of the SQL pattern within the time range to query.
        #     *   `AverageScanSize`: the average amount of data scanned based on the SQL pattern within the time range to query.
        #     *   `MaxScanSize`: the maximum amount of data scanned based on the SQL pattern within the time range to query.
        #     *   `QueryCount`: the number of queries performed in association with the SQL pattern within the time range to query.
        #     *   `FailedCount`: the number of failed queries performed in association with the SQL pattern within the time range to query.
        # 
        # *   `Type` specifies the sorting order. Valid values (case-insensitive):
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # This parameter is required.
        self.order = order
        # The page number. Pages start from page 1.
        # 
        # > If you do not specify this parameter, the value **1** is used.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # > If you do not specify this parameter, the value **30** is used.
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.sql_pattern_hash = sql_pattern_hash
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > 
        # 
        # *   Only data within the last 14 days can be queried. For example, if the current time is 2021-11-22T12:00:00Z, you can query SQL patterns at a point in time as early as 2021-11-09T12:00:00Z.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        # 
        # This parameter is required.
        self.start_time = start_time
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

