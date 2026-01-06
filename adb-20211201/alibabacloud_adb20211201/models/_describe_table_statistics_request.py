# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTableStatisticsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        keyword: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        schema_name: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The keyword that is used to query information by table name.
        self.keyword = keyword
        # The order by which to sort query results. Specify the parameter value in the JSON format.
        # 
        # Example:
        # 
        #     [
        # 
        #         {
        # 
        #             "Field":"Name",
        # 
        #             "Type":"Asc"
        # 
        #         }
        # 
        #     ]
        # 
        # Field specifies the field by which to sort the query results. Set the value to Name. Type specifies the sorting order. Valid values: Desc and Asc.
        # 
        # Field and Type are case-insensitive.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612393.html) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the database.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        return self

