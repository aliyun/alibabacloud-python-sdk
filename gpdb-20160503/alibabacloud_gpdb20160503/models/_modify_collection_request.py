# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCollectionRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        metadata: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The collection name.
        # 
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to list all collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query details for all AnalyticDB for PostgreSQL instances in a region, including their instance IDs.
        self.dbinstance_id = dbinstance_id
        # A JSON string that specifies the operations to add or modify metadata fields. For the required format, see the example.
        # 
        # Use this parameter to add new metadata fields, rename existing metadata fields, or perform implicit data type conversion on existing fields.
        # 
        # Details:
        # 
        # To add a new metadata field, set `operations[*].operator = add`. Then, use `operations[*].newMetaName` to specify the field\\"s name, `operations[*].newMetaType` for its data type, and `operations[*].fullTextRetrieval` to enable full-text retrieval for it.
        # 
        # To modify an existing metadata field, set `operations[*].operator = replace`. You must specify the current field name in `operations[*].oldMetaName`. To rename the field, provide the new name in `operations[*].newMetaName`. To change its data type, provide the new type in `operations[*].newMetaType`.
        # 
        # > - For a list of supported data types, see [Data types](https://help.aliyun.com/document_detail/424383.html). The money data type is not supported.
        # >
        # > - Full-text retrieval can be enabled for a field only during an `add` operation, not a `replace` operation.
        # 
        # >Warning: 
        # 
        # The field names `id`, `vector`, `to_tsvector`, and `source` are reserved.
        # 
        # This parameter is required.
        self.metadata = metadata
        # The namespace. The default value is `public`.
        # 
        # > You can call the CreateNamespace operation to create a namespace and the ListNamespaces operation to list existing namespaces.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the workspace that contains multiple database instances. You must specify either this parameter or `DBInstanceId`. If you specify both, this parameter takes precedence.
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

