# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosisRecordsRequest(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        dbcluster_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        max_peak_memory: int = None,
        max_scan_size: int = None,
        min_peak_memory: int = None,
        min_scan_size: int = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        pattern_id: str = None,
        query_condition: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        # The source IP address.
        # 
        # > Call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to view the resource groups, database names, usernames, and source IP addresses for the SQL statements that meet the specified query conditions.
        self.client_ip = client_ip
        # The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to view the details of all clusters in your account, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database where the SQL statement is executed.
        # 
        # > Call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to view the resource groups, database names, usernames, and source IP addresses for the SQL statements that meet the specified query conditions.
        self.database = database
        # The end of the time range to query. Specify the time in the UNIX timestamp format. The time must be in milliseconds.
        # 
        # > - The end time must be later than the start time.
        # >
        # > - The interval between the start time and the end time cannot exceed 24 hours.
        self.end_time = end_time
        # Filters the queries by the keywords contained in the SQL statements.
        self.keyword = keyword
        # The language of the file title and some error messages in the downloaded file. Valid values:
        # 
        # - **zh**: Simplified Chinese (default).
        # 
        # - **en**: English.
        # 
        # - **ja**: Japanese.
        # 
        # - **zh-tw**: Traditional Chinese.
        self.lang = lang
        # The maximum peak memory of the SQL statement. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum scan size of the target SQL statement. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The minimum peak memory of the SQL statement. Unit: bytes.
        self.min_peak_memory = min_peak_memory
        # The minimum scan size of the SQL statement. Unit: bytes.
        self.min_scan_size = min_scan_size
        # The sorting order of the SQL statements. This parameter is a JSON array that is ordered by the sequence of the input array. It contains the `Field` and `Type` fields. Example: `[{"Field":"StartTime", "Type": "desc" }]`. The fields are described as follows:
        # 
        # - `Field` specifies the field by which to sort the SQL statements. Valid values:
        # 
        #   - `StartTime`: the start time of the execution.
        # 
        #   - `Status`: the execution state.
        # 
        #   - `UserName`: the username.
        # 
        #   - `Cost`: the execution duration.
        # 
        #   - `PeakMemory`: the peak memory.
        # 
        #   - `ScanSize`: the amount of scanned data.
        # 
        #   - `Database`: the database name.
        # 
        #   - `ClientIp`: the source IP address.
        # 
        #   - `ResourceGroup`: the resource group.
        # 
        #   - `QueueTime`: the amount of time that the query waited in a queue.
        # 
        #   - `OutputRows`: the number of output rows.
        # 
        #   - `OutputDataSize`: the amount of output data.
        # 
        #   - `ResourceCostRank`: the ranking of the execution duration of an operator in the SQL statement. This field is returned only when `QueryCondition` is set to `{"Type":"status","Value":"running"}`.
        # 
        # - `Type` specifies the sorting type. Valid values (case-insensitive):
        # 
        #   - `Desc`: descending order.
        # 
        #   - `Asc`: ascending order.
        self.order = order
        # The page number. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **30** (default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The ID of the SQL pattern.
        self.pattern_id = pattern_id
        # The conditions for the SQL query. This parameter is a JSON string that contains fields such as Type, `Value`, `Min`, and `Max`. The `Type` field indicates the query dimension. Valid values for `Type`: `maxCost`, `status`, and `cost`. The `Value`, `Min`, and `Max` fields specify the query range for the dimension. Valid values:
        # 
        # - `{"Type":"maxCost","Value":"100"}`: queries the details of the top 100 SQL statements that have the longest execution durations. The `Value` field can only be set to 100.
        # 
        # - `{"Type":"status","Value":"finished"}`: queries the details of completed SQL statements. You can also set `Value` to `running` or `failed` to query SQL statements that are running or have failed.
        # 
        # - `{"Type":"cost","Min":"10","Max":"200"}`: queries the details of SQL statements whose execution durations are between 10 ms and 200 ms. You can customize the minimum and maximum execution durations. Unit: milliseconds.
        self.query_condition = query_condition
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to view the regions and zones supported by AnalyticDB for MySQL, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group to which the SQL statement belongs.
        # 
        # > Call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to view the resource groups, database names, usernames, and source IP addresses for the SQL statements that meet the specified query conditions.
        self.resource_group = resource_group
        # The start of the time range to query. Specify the time in the UNIX timestamp format. The time must be in milliseconds.
        # 
        # > Only data from the last 14 days can be queried.
        self.start_time = start_time
        # The username used to execute the SQL statement.
        # Call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to view the resource groups, database names, usernames, and source IP addresses for the SQL statements that meet the specified query conditions.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.database is not None:
            result['Database'] = self.database

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory

        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size

        if self.min_peak_memory is not None:
            result['MinPeakMemory'] = self.min_peak_memory

        if self.min_scan_size is not None:
            result['MinScanSize'] = self.min_scan_size

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id

        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')

        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')

        if m.get('MinPeakMemory') is not None:
            self.min_peak_memory = m.get('MinPeakMemory')

        if m.get('MinScanSize') is not None:
            self.min_scan_size = m.get('MinScanSize')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')

        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

