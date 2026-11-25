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
        # > You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource group, database name, username, and source IP address of the SQL statements that meet the specified search conditions.
        self.client_ip = client_ip
        # The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to query the details of all clusters under your account, including the cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database in which the SQL statement is executed.
        # > You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource group, database name, username, and source IP address of the SQL statements that meet the specified search conditions.
        self.database = database
        # The end time of the query. The time is a UNIX timestamp in milliseconds.
        # > * The end time must be later than the start time.
        # > * The interval between the start time and the end time cannot exceed 24 hours.
        self.end_time = end_time
        # The keyword used to filter SQL statements.
        self.keyword = keyword
        # The language of the downloaded file title and some error messages. Valid values:
        # - **zh**: Simplified Chinese (default).
        # - **en**: English.
        # - **ja**: Japanese.
        # - **zh-tw**: Traditional Chinese.
        self.lang = lang
        # The Peak Volume of memory for the SQL statement. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum scan size of the SQL statement. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The minimum peak memory of the SQL statement. Unit: bytes.
        self.min_peak_memory = min_peak_memory
        # The minimum scan size of the SQL statement. Unit: bytes.
        self.min_scan_size = min_scan_size
        # The sorting rules for SQL statements based on specified fields. The value is a JSON array that contains the Field and Type fields. The SQL statements are sorted in the order of the fields in the array. Example: `[{"Field":"StartTime", "Type": "desc" }]`.
        # - Field: the name of the field by which you want to sort the SQL statements. Valid values:
        #     - StartTime: the start time of the execution.
        #     - Status: the execution status.
        #     - UserName: the username.
        #     - Cost: the execution duration.
        #     - PeakMemory: the peak memory.
        #     - ScanSize: the scan size.
        #     - Database: the database name.
        #     - ClientIp: the source IP address.
        #     - ResourceGroup: the resource group.
        #     - QueueTime: the queue time.
        #     - OutputRows: the number of output rows.
        #     - OutputDataSize: the output data size.
        #     - ResourceCostRank: the ranking of the execution duration of internal operators in the SQL statement. This field is supported only when QueryCondition is set to `{"Type":"status","Value":"running"}`.
        # - Type: the sorting type. Valid values (case-insensitive):
        #     - Desc: descending order.
        #     - Asc: ascending order.
        self.order = order
        # The page number. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - **30** (default)
        # - **50**
        # - **100**
        self.page_size = page_size
        # The ID of the SQL pattern.
        self.pattern_id = pattern_id
        # The conditions for the SQL query. The value is a JSON string that contains fields such as Type, Value, Min, and Max. The Type field specifies the query dimension. Valid values: maxCost, status, and cost. The Value, Min, or Max field specifies the query range for the dimension. Valid values:
        # - `{"Type":"maxCost","Value":"100"}`: queries the details of the top 100 SQL statements with the longest execution duration. Currently, the Value field can only be set to 100.
        # - `{"Type":"status","Value":"finished"}`: queries the details of completed SQL statements. You can also set Value to running or failed to query the details of running or failed SQL statements.
        # - `{"Type":"cost","Min":"10","Max":"200"}`: queries the details of SQL statements whose execution duration is between 10 milliseconds and 200 milliseconds. You can also customize the maximum and minimum execution duration in milliseconds.
        self.query_condition = query_condition
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the regions and zones supported by AnalyticDB for MySQL, including the region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group to which the SQL statement belongs.
        # > You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource group, database name, username, and source IP address of the SQL statements that meet the specified search conditions.
        self.resource_group = resource_group
        # The start time of the query. The time is a UNIX timestamp in milliseconds.
        # > You can only query data within the last 14 days.
        self.start_time = start_time
        # The username that executes the SQL statement.
        # You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource group, database name, username, and source IP address of the SQL statements that meet the specified search conditions.
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

