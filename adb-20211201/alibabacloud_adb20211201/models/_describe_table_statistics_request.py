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
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The search keyword. Fuzzy search by table name is supported.
        self.keyword = keyword
        # The sorting rule for a specified field. The value is a JSON array. The array is ordered. Specify the fields to be sorted and the sorting order in sequence:
        # 
        # For example:
        # 
        # ```
        # [
        # 
        #     {
        # 
        #         "Field":"Name",
        # 
        #         "Type":"Asc"
        # 
        #     }
        # 
        # ]
        # ```
        # 
        # Field specifies the name of the field to be sorted. Only the Name field is supported.
        # Type specifies the sorting order. Desc indicates descending order, and Asc indicates ascending order.
        # 
        # Both parameters are case-insensitive.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612393.html) operation to query the region ID.
        self.region_id = region_id
        # The database name.
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

