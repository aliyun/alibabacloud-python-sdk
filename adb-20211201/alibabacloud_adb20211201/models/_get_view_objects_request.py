# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetViewObjectsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        filter_owner: str = None,
        filter_view_name: str = None,
        filter_view_type: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        schema_name: str = None,
        show_mv_base_table: bool = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The owner of the view.
        self.filter_owner = filter_owner
        # The name of the view.
        self.filter_view_name = filter_view_name
        # The type of the view.
        # 
        # Valid values:
        # 
        # \\-VIRTUAL_VIEW
        # 
        # \\-MATERIALIZED_VIEW
        # 
        # Default value: null.
        self.filter_view_type = filter_view_type
        # The order in which you want to sort the query results. Valid values for Type:
        # 
        # *   Asc
        # *   Desc
        # 
        # Valid values for Field: -ViewName
        # 
        # \\-CreateTime
        # 
        # \\-UpdateTime
        # 
        # Default value: {"Type": "Desc","Field": "ViewName"}.
        self.order_by = order_by
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the database.
        self.schema_name = schema_name
        self.show_mv_base_table = show_mv_base_table

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

        if self.filter_view_name is not None:
            result['FilterViewName'] = self.filter_view_name

        if self.filter_view_type is not None:
            result['FilterViewType'] = self.filter_view_type

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

        if self.show_mv_base_table is not None:
            result['ShowMvBaseTable'] = self.show_mv_base_table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FilterOwner') is not None:
            self.filter_owner = m.get('FilterOwner')

        if m.get('FilterViewName') is not None:
            self.filter_view_name = m.get('FilterViewName')

        if m.get('FilterViewType') is not None:
            self.filter_view_type = m.get('FilterViewType')

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

        if m.get('ShowMvBaseTable') is not None:
            self.show_mv_base_table = m.get('ShowMvBaseTable')

        return self

