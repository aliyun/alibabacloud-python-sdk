# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadDiagnosisRecordsRequest(DaraModel):
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
        query_condition: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        # The source IP address.
        # 
        # >  You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource groups, database names, usernames, and source IP addresses of the SQL statements that meet a query condition.
        self.client_ip = client_ip
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database on which the SQL statements are executed.
        # 
        # >  You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource groups, database names, usernames, and source IP addresses of the SQL statements that meet a query condition.
        self.database = database
        # The end of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        self.end_time = end_time
        # The query keyword of the SQL statements.
        self.keyword = keyword
        # The language. Valid values:
        # 
        # *   **zh**: simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The maximum peak memory of the SQL statements. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum scan size of the SQL statements. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The minimum peak memory of the SQL statements. Unit: bytes.
        self.min_peak_memory = min_peak_memory
        # The minimum scan size of the SQL statements. Unit: bytes.
        self.min_scan_size = min_scan_size
        # The query condition for SQL statements, which can contain the `Type`, `Value`, `Min`, and `Max` fields. Specify the condition in the JSON format. `Type` specifies the query dimension. Valid values for Type: `maxCost`, `status`, and `cost`. `Value`, `Min`, or `Max` specifies the query range for the dimension. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"100"}`: queries the top 100 most time-consuming SQL statements. Set `Value` to 100.
        # *   `{"Type":"status","Value":"finished"}`: queries the executed SQL statements. You can set `Value` to `running` to query the SQL statements that are being executed. You can also set Value to `failed` to query the SQL statements that failed to be executed.
        # *   `{"Type":"cost","Min":"10","Max":"200"}`: queries the SQL statements whose execution duration is in the range of 10 to 200 milliseconds. You can also specify custom values for the Min and Max fields.
        self.query_condition = query_condition
        # The region ID of the cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group to which the SQL statements belong.
        # 
        # >  You can call the [DescribeDiagnosisDimensions](https://help.aliyun.com/document_detail/308210.html) operation to query the resource groups, database names, usernames, and source IP addresses of the SQL statements that meet a query condition.
        self.resource_group = resource_group
        # The beginning of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  You can query data only within the last 14 days.
        self.start_time = start_time
        # The username that is used to execute the SQL statements.
        # 
        # >  You can call the [DescribeDiagnosisDimensions](~~~~) operation to query the resource groups, database names, usernames, and source IP addresses of the SQL statements that meet a query condition.
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

