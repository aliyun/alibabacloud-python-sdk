# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteChunksRequest(DaraModel):
    def __init__(
        self,
        chunk_ids: List[str] = None,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        region_id: str = None,
    ):
        # A list of chunk IDs.
        # 
        # This parameter is required.
        self.chunk_ids = chunk_ids
        # The name of the document collection.
        # 
        # > You create this document collection by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. To view existing document collections, call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > Call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to view details for all AnalyticDB for PostgreSQL instances in a specific region, including their instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the namespace. The default value is public.
        # 
        # > Call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to view a list of namespaces.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # > This password is set when you call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The region ID of the instance.
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
        if self.chunk_ids is not None:
            result['ChunkIds'] = self.chunk_ids

        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkIds') is not None:
            self.chunk_ids = m.get('ChunkIds')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

