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
        # The name of the collection.
        # 
        # >  You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to query a list of collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The metadata of the addition or modification operation, which is in the JSON string format.
        # 
        # You can specify this parameter to add a metadata definition, or rename an existing metadata definition and perform implicit type conversion.
        # 
        # If you specify `operations[*].operator = add` to add a metadata definition, `operations[*].newMetaName` specifies the name of the metadata definition, and `operations[*].newMetaType` specifies the data type of the metadata definition.
        # 
        # If you specify `operations[*].operator = replace` to modify an existing metadata definition, `operations[*].oldMetaName` specifies the current name of the metadata definition, `operations[*].newMetaName` specifies the new name of the metadata definition, and `operations[*].newMetaType` specifies the new data type of the metadata definition. If you only want to rename the metadata definition, you do not need to specify the `operations[*].newMetaType` field. If you only want to perform implicit type conversion, you do not need to specify the `operations[*].newMetaName` field.
        # 
        # > 
        # 
        # *   For information about the supported data types, see [Data types](https://help.aliyun.com/document_detail/424383.html).
        # 
        # *   The money data type is not supported.
        # 
        # **
        # 
        # **Warning**Reserved fields such as id, vector, to_tsvector, and source cannot be used.
        # 
        # This parameter is required.
        self.metadata = metadata
        # The name of the namespace. Default value: public.
        # 
        # >  You can call the CreateNamespace operation to create a namespace and call the ListNamespaces operation to query a list of namespaces.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the workspace that consists of multiple AnalyticDB for PostgreSQL instances. You must specify one of the WorkspaceId and DBInstanceId parameters. If you specify both parameters, the WorkspaceId parameter takes precedence.
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

