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
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all clusters in a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Sorts the query results by a specified field. The value is a JSON string. Example: `[{"Field":"TableSchema","Type":"Asc"}]`.
        # - `Field` specifies the field by which to sort. Valid values:
        #     - `TableSchema`: the name of the database to which the table belongs.
        #     - `TableName`: the table name.
        #     - `AccessCount`: the number of times the table is accessed.
        # - `Type` specifies the sort order. Valid values:
        #     - `Asc`: ascending order.
        #     - `Desc`: descending order.
        # 
        # > If this parameter is not specified, the results are sorted by the database name of the table in ascending order by default.
        self.order = order
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - **10** (default)
        # - **30**
        # - **50**
        # - **100**
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query, in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        # > Only data within the last 30 days can be queried.
        self.start_time = start_time
        # The name of the table.
        # > If this parameter is left empty, the access frequency data of all tables in the cluster within the specified date range is returned.
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

