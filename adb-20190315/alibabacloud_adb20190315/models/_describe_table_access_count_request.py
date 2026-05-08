# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTableAccessCountRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
        table_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the details of all AnalyticDB for MySQL clusters within a specified region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The order by which to sort query results. Specify the parameter value in the JSON string format. Example: `[{"Field":"TableSchema","Type":"Asc"}]`.
        # 
        # *   `Field` indicates the field that is used to sort the retrieved entries. Valid values:
        # 
        #     *   `TableSchema`: the name of the database to which the table belongs.
        #     *   `TableName`: the name of the table.
        #     *   `AccessCount`: the number of accesses to the table.
        # 
        # *   `Type` indicates the sorting method. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # >  If this parameter is not specified, query results are sorted in ascending order of the database to which a specific table belongs.
        self.order = order
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The value must be a positive integer. Default value: **30**.
        self.page_size = page_size
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the regions and zones supported by AnalyticDB for MySQL, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The date to query. Specify the time in the *yyyy-MM-dd* format. The time must be in UTC.
        # 
        # >  Only data for the last 30 days can be queried.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the specific table.
        # 
        # >  If this parameter is not specified, the number of accesses to all tables within the specified cluster for a specified date is returned.
        self.table_name = table_name

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.table_name is not None:
            result['TableName'] = self.table_name

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

