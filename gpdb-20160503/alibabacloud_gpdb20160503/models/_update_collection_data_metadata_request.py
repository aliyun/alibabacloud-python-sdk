# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class UpdateCollectionDataMetadataRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        filter: str = None,
        ids: List[str] = None,
        metadata: Dict[str, Any] = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # Collection name.
        # 
        # > You can use the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) API to view the list.
        # 
        # This parameter is required.
        self.collection = collection
        # Instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) API to view details of all AnalyticDB for PostgreSQL instances in the target region, including the instance ID.
        self.dbinstance_id = dbinstance_id
        # Filter condition for the data to be updated, in SQL WHERE format. This field cannot be empty at the same time as the Ids field.
        self.filter = filter
        # ID list of the data to be updated, i.e., the Row.Id specified when uploading the data. This field cannot be empty at the same time as the Filter field.
        self.ids = ids
        # Data to be updated, in a JSON string of MAP format. The key is the field name, and the value is the new data value.
        # 
        # This parameter is required.
        self.metadata = metadata
        # Namespace.
        # 
        # > You can use the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) API to view the list.
        self.namespace = namespace
        # Password corresponding to the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # Region ID where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # ID of the Workspace composed of multiple database instances. This parameter and the DBInstanceId parameter cannot both be empty. When both are specified, this parameter takes precedence.
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

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.metadata is not None:
            result['Metadata'] = self.metadata

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

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

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

