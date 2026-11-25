# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosisDimensionsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        lang: str = None,
        query_condition: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition (3.0) clusters in the specified region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time as a UNIX timestamp in milliseconds.
        # 
        # > * The end time must be later than the start time.
        # > * The interval between the start time and the end time cannot exceed 24 hours.
        self.end_time = end_time
        # The language configuration. Valid values:
        # - **zh-CN**: Simplified Chinese (default).
        # - **en-US**: English.
        # - **ja**: Japanese.
        self.lang = lang
        # The search conditions for SQL queries. The value is a JSON string that contains fields such as `Type`, `Value`, `Min`, and `Max`. The `Type` field specifies the query dimension. Valid values: `maxCost`, `status`, and `cost`. The `Value`, `Min`, or `Max` field specifies the query range for the dimension. Valid values:
        # - `{"Type":"maxCost","Value":"100"}`: queries the details of the top 100 SQL statements with the longest execution duration. Currently, you can only set `Value` to 100.
        # - `{"Type":"status","Value":"finished"}`: queries the details of completed SQL statements. You can also set `Value` to `running` or `failed` to query the details of running or failed SQL statements.
        # - `{"Type":"cost","Min":"10","Max":"200"}`: queries the details of SQL statements whose execution duration is between 10 milliseconds and 200 milliseconds. You can also customize the minimum and maximum execution duration in milliseconds.
        self.query_condition = query_condition
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the region ID of the specified AnalyticDB for MySQL Data Lakehouse Edition (3.0) cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time of the query. Specify the time as a UNIX timestamp in milliseconds.
        # > You can only query data from the last 14 days. If you query data from more than 14 days ago, an empty result is returned.
        self.start_time = start_time

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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

