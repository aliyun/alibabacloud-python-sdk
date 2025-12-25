# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDataLakePartitionRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        data_region: str = None,
        db_name: str = None,
        if_exists: bool = None,
        partition_values: List[str] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # The name of the data catalog.
        # 
        # This parameter is required.
        self.catalog_name = catalog_name
        # The region where the data lake resides.
        # 
        # This parameter is required.
        self.data_region = data_region
        # The name of the database that you want to query.
        # 
        # This parameter is required.
        self.db_name = db_name
        # Specifies whether to ignore the exception if the partition that you want to delete does not exist.
        self.if_exists = if_exists
        # The values in a partition key column.
        # 
        # This parameter is required.
        self.partition_values = partition_values
        # The table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the DMS console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.if_exists is not None:
            result['IfExists'] = self.if_exists

        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')

        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

