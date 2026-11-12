# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCollectionDataRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        collection_data: str = None,
        collection_data_filter: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The collection name.
        # 
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to view the list.
        # 
        # This parameter is required.
        self.collection = collection
        # The data fields and values to delete. The value is a JSON string in dictionary format, where the key is the field name and the value is a list of data values to delete.
        self.collection_data = collection_data
        # The filter condition for the data to delete. The format is SQL WHERE syntax.
        self.collection_data_filter = collection_data_filter
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to view the IDs of all AnalyticDB for PostgreSQL instances in the target region.
        self.dbinstance_id = dbinstance_id
        # The namespace. Default value: public.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to view the list.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to view the available region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the workspace that consists of multiple database instances. This parameter and the DBInstanceId parameter cannot be empty at the same time. If both parameters are specified, this parameter takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.collection_data is not None:
            result['CollectionData'] = self.collection_data

        if self.collection_data_filter is not None:
            result['CollectionDataFilter'] = self.collection_data_filter

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('CollectionData') is not None:
            self.collection_data = m.get('CollectionData')

        if m.get('CollectionDataFilter') is not None:
            self.collection_data_filter = m.get('CollectionDataFilter')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

