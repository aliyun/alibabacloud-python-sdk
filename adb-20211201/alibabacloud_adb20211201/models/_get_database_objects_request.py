# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatabaseObjectsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        filter_owner: str = None,
        filter_schema_name: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The owner.
        self.filter_owner = filter_owner
        # The database name.
        self.filter_schema_name = filter_schema_name
        # The sort field.
        # Valid values for Type:
        # - Asc
        # - Desc
        # 
        # Valid values for Field:
        # - DatabseName
        # - CreateTime
        # - UpdateTime
        # 
        # Default value: {"Type": "Desc","Field": "DatabaseName"}.
        self.order_by = order_by
        # The page number. The value must be greater than 0 and no greater than the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - 30
        # - 50
        # - 100
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.filter_owner is not None:
            result['FilterOwner'] = self.filter_owner

        if self.filter_schema_name is not None:
            result['FilterSchemaName'] = self.filter_schema_name

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FilterOwner') is not None:
            self.filter_owner = m.get('FilterOwner')

        if m.get('FilterSchemaName') is not None:
            self.filter_schema_name = m.get('FilterSchemaName')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

