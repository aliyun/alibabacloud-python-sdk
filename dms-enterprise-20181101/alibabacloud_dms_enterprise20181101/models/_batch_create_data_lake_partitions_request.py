# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class BatchCreateDataLakePartitionsRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        data_region: str = None,
        db_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_inputs: List[main_models.DLPartitionInput] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # The catalog name.
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
        # Specifies whether to ignore this exception if the name of the new partition is the same as that of an existing partition. Valid values:
        # 
        # *   true: Ignore the exception.
        # *   false: Do not ignore the exception.
        self.if_not_exists = if_not_exists
        # Specifies whether to return partition information. If the value is true, Partitions is returned.
        self.need_result = need_result
        # The information about the new partitions.
        # 
        # This parameter is required.
        self.partition_inputs = partition_inputs
        # The name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.partition_inputs:
            for v1 in self.partition_inputs:
                 if v1:
                    v1.validate()

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

        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists

        if self.need_result is not None:
            result['NeedResult'] = self.need_result

        result['PartitionInputs'] = []
        if self.partition_inputs is not None:
            for k1 in self.partition_inputs:
                result['PartitionInputs'].append(k1.to_map() if k1 else None)

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

        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')

        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')

        self.partition_inputs = []
        if m.get('PartitionInputs') is not None:
            for k1 in m.get('PartitionInputs'):
                temp_model = main_models.DLPartitionInput()
                self.partition_inputs.append(temp_model.from_map(k1))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

