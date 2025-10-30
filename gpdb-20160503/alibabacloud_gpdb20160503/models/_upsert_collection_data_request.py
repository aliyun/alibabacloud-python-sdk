# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class UpsertCollectionDataRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        rows: List[main_models.UpsertCollectionDataRequestRows] = None,
        workspace_id: str = None,
    ):
        # The name of the collection.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the namespace. Default value: public.
        # 
        # >  You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query a list of namespaces.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.rows = rows
        # The ID of the workspace that consists of multiple AnalyticDB for PostgreSQL instances. You must specify one of the WorkspaceId and DBInstanceId parameters. If you specify both parameters, the WorkspaceId parameter takes effect.
        self.workspace_id = workspace_id

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

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

        result['Rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['Rows'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

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

        self.rows = []
        if m.get('Rows') is not None:
            for k1 in m.get('Rows'):
                temp_model = main_models.UpsertCollectionDataRequestRows()
                self.rows.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpsertCollectionDataRequestRows(DaraModel):
    def __init__(
        self,
        id: str = None,
        metadata: Dict[str, str] = None,
        sparse_vector: main_models.UpsertCollectionDataRequestRowsSparseVector = None,
        vector: List[float] = None,
    ):
        self.id = id
        self.metadata = metadata
        self.sparse_vector = sparse_vector
        # This parameter is required.
        self.vector = vector

    def validate(self):
        if self.sparse_vector:
            self.sparse_vector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.sparse_vector is not None:
            result['SparseVector'] = self.sparse_vector.to_map()

        if self.vector is not None:
            result['Vector'] = self.vector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('SparseVector') is not None:
            temp_model = main_models.UpsertCollectionDataRequestRowsSparseVector()
            self.sparse_vector = temp_model.from_map(m.get('SparseVector'))

        if m.get('Vector') is not None:
            self.vector = m.get('Vector')

        return self

class UpsertCollectionDataRequestRowsSparseVector(DaraModel):
    def __init__(
        self,
        indices: List[int] = None,
        values: List[float] = None,
    ):
        self.indices = indices
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.indices is not None:
            result['Indices'] = self.indices

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Indices') is not None:
            self.indices = m.get('Indices')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

