# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableObjectsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        filter_description: str = None,
        filter_owner: str = None,
        filter_tbl_name: str = None,
        filter_tbl_type: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        schema_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The description of the table.
        self.filter_description = filter_description
        # The owner of the table.
        self.filter_owner = filter_owner
        # The name of the table.
        self.filter_tbl_name = filter_tbl_name
        # The type of the table.
        # 
        # Valid values:
        # 
        # DIMENSION_TABLE
        # 
        # FACT_TABLE
        # 
        # EXTERNAL_TABLE
        # 
        # Default value: null.
        self.filter_tbl_type = filter_tbl_type
        # The order in which the fields to be returned are sorted.
        # 
        # Valid values:
        # 
        # *   Asc
        # *   Desc
        # 
        # Values for fields:
        # 
        # TableName
        # 
        # TableSize
        # 
        # CreateTime
        # 
        # UpdateTime
        # 
        # Default value: {"Type": "Desc","Field": "TableName"};
        self.order_by = order_by
        # The number of the page to return. The value is an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # Default value: 30.
        self.page_size = page_size
        # The ID of the region in which the cluster resides.
        # 
        # This parameter is required.
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

        if self.filter_description is not None:
            result['FilterDescription'] = self.filter_description

        if self.filter_owner is not None:
            result['FilterOwner'] = self.filter_owner

        if self.filter_tbl_name is not None:
            result['FilterTblName'] = self.filter_tbl_name

        if self.filter_tbl_type is not None:
            result['FilterTblType'] = self.filter_tbl_type

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

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

        if m.get('FilterDescription') is not None:
            self.filter_description = m.get('FilterDescription')

        if m.get('FilterOwner') is not None:
            self.filter_owner = m.get('FilterOwner')

        if m.get('FilterTblName') is not None:
            self.filter_tbl_name = m.get('FilterTblName')

        if m.get('FilterTblType') is not None:
            self.filter_tbl_type = m.get('FilterTblType')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        return self

