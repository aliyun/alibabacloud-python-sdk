# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVectorIndexRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        external_storage: int = None,
        hnsw_ef_construction: int = None,
        hnsw_m: int = None,
        manager_account: str = None,
        manager_account_password: str = None,
        metrics: str = None,
        namespace: str = None,
        owner_id: int = None,
        pq_enable: int = None,
        region_id: str = None,
        type: str = None,
    ):
        # Collection name.
        # > You can use the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) API to view the list.
        # 
        # This parameter is required.
        self.collection = collection
        # Instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) API to view details of all AnalyticDB PostgreSQL instances in the target region, including the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Vector dimension.
        # > This value must be consistent with the length of the vector data (Rows. Vector) uploaded via the [UpsertCollectionData](https://help.aliyun.com/document_detail/2401493.html) API.
        self.dimension = dimension
        # Whether to use mmap to build the HNSW index, default is 0. If the data does not need to be deleted and there are performance requirements for uploading data, it is recommended to set this to 1.
        # 
        # > 
        # > - When set to 0, the segment-page storage mode is used to build the index, which can use the shared_buffer in PostgreSQL for caching and supports deletion and update operations.
        # > - When set to 1, the index is built using mmap, which does not support deletion and update operations.
        self.external_storage = external_storage
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors in the HNSW algorithm, ranging from 1 to 1000. The API will automatically set this value based on the vector dimension, and it generally does not need to be manually set.
        # 
        # > It is suggested to set this based on the vector dimension as follows:
        # > - Less than or equal to 384: 16
        # > - Greater than 384 and less than or equal to 768: 32
        # > - Greater than 768 and less than or equal to 1024: 64
        # > - Greater than 1024: 128
        self.hnsw_m = hnsw_m
        # Name of the management account with rds_superuser permissions.
        # 
        # > You can create an account through the console -> Account Management, or by using the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) API.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # Management account password.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # Method used for building the vector index. Value description:
        # - l2: Euclidean distance.
        # - ip: Inner product (dot product) distance.
        # - cosine: Cosine similarity.
        self.metrics = metrics
        # Namespace, default is public.
        # 
        # > You can use the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) API to view the list.
        self.namespace = namespace
        self.owner_id = owner_id
        # Whether to enable PQ (Product Quantization) algorithm acceleration for the index. It is recommended to enable this when the data volume exceeds 500,000. Value description:
        # - 0: Disabled.
        # - 1: Enabled (default).
        self.pq_enable = pq_enable
        # Region ID where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.type = type

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

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.external_storage is not None:
            result['ExternalStorage'] = self.external_storage

        if self.hnsw_ef_construction is not None:
            result['HnswEfConstruction'] = self.hnsw_ef_construction

        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m

        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account

        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('ExternalStorage') is not None:
            self.external_storage = m.get('ExternalStorage')

        if m.get('HnswEfConstruction') is not None:
            self.hnsw_ef_construction = m.get('HnswEfConstruction')

        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')

        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')

        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

